from py3dbp import Packer, Bin, Item
from box_manager.models import Box
from django.db.models import F, Exists, ExpressionWrapper, FloatField, OuterRef
from django.db.models.functions import Now, Extract
from core_utils.Logger import Logger



Log = Logger()

class box_handler():

    def __call__(self, data):

        try:

            cart_items = data.get('items')

            items_to_pack = []
            
            for items in cart_items:
                item_added = 0
                while int(items.get('quantity')) > item_added:
                    items_to_pack.append(items)
                    item_added +=1

            avail_boxes = Box.objects.all()


            possible_boxes = []
            
            for box in avail_boxes:
                packer = Packer()
                packer.add_bin(
                        Bin(
                            name=box.name,
                            width=box.width,
                            depth=box.length,
                            height=box.height,
                            max_weight=box.max_weight
                            )
                        )

                for item in items_to_pack:
                    packer.add_item(
                            Item(
                                name=item.get('name'),
                                width=item.get('width'),
                                height=item.get('height'),
                                depth=item.get('length'),
                                weight=item.get('weight')
                                )
                            )
                    

                packer.pack(bigger_first=True, distribute_items=False)


                box = packer.bins[0]
                Log.Log_Debug('Evaluating Box:', box.name)
                Log.Log_Debug('  Fitted items:', len(box.items))
                Log.Log_Debug('  Unfitted items:', len(box.unfitted_items))
                
                if not box.unfitted_items and box.items:
                    possible_boxes.append(box.name)
                    
                    for packed_item in box.items:
                        Log.Log_Debug(f"{packed_item.name} packed at {packed_item.position} with rotation",  {packed_item.rotation_type})



            Log.Log_Debug('Successful Boxes that can fit the whole order:', possible_boxes)


            Log.Log_Debug('possible boxes', possible_boxes)

            

            box_price_list = avail_boxes.filter(
                    name__in = possible_boxes
                    ).order_by('cost')
            Log.Log_Debug('box price list', box_price_list)


            if len(box_price_list)==0:
                return{
                        'code':'not-possible-in-single-box'
                        }
            else:
                best_box = box_price_list[0]
                return {
                        'name':best_box.name,
                        'cost':best_box.cost,
                        'weight':best_box.max_weight
                        }

        except Exception as e:
            Log.Log_Error('box-handler-callback-exception', e)
