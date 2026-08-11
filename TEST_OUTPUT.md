(env) ➜  ai_power_box_selection git:(main) ✗ python manage.py test

Found 4 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).

 Log ---> Evaluating Box:,
Debug Code --> Test Medium Box


 Log --->   Fitted items:,
Debug Code --> 0


 Log --->   Unfitted items:,
Debug Code --> 1


 Log ---> Successful Boxes that can fit the whole order:,
Debug Code --> []


 Log ---> possible boxes,
Debug Code --> []


 Log ---> box price list,
Debug Code --> <QuerySet []>

.
 Log ---> Evaluating Box:,
Debug Code --> Test Medium Box


 Log --->   Fitted items:,
Debug Code --> 0


 Log --->   Unfitted items:,
Debug Code --> 1


 Log ---> Successful Boxes that can fit the whole order:,
Debug Code --> []


 Log ---> possible boxes,
Debug Code --> []


 Log ---> box price list,
Debug Code --> <QuerySet []>

.
 Log ---> Evaluating Box:,
Debug Code --> Test Medium Box


 Log --->   Fitted items:,
Debug Code --> 4


 Log --->   Unfitted items:,
Debug Code --> 0


 Log ---> Rubiks Cube packed at [0, 0, 0] with rotation,
Debug Code --> {0}


 Log ---> Rubiks Cube packed at [Decimal('5.000'), 0, 0] with rotation,
Debug Code --> {0}


 Log ---> Rubiks Cube packed at [Decimal('10.000'), 0, 0] with rotation,
Debug Code --> {0}


 Log ---> Rubiks Cube packed at [Decimal('15.000'), 0, 0] with rotation,
Debug Code --> {0}


 Log ---> Successful Boxes that can fit the whole order:,
Debug Code --> ['Test Medium Box']


 Log ---> possible boxes,
Debug Code --> ['Test Medium Box']


 Log ---> box price list,
Debug Code --> <QuerySet [<Box: Box object (1)>]>

.
 Log ---> Evaluating Box:,
Debug Code --> Test Medium Box


 Log --->   Fitted items:,
Debug Code --> 1


 Log --->   Unfitted items:,
Debug Code --> 0


 Log ---> Mouse packed at [0, 0, 0] with rotation,
Debug Code --> {0}


 Log ---> Successful Boxes that can fit the whole order:,
Debug Code --> ['Test Medium Box']


 Log ---> possible boxes,
Debug Code --> ['Test Medium Box']


 Log ---> box price list,
Debug Code --> <QuerySet [<Box: Box object (1)>]>

.
----------------------------------------------------------------------
Ran 4 tests in 0.010s

OK
Destroying test database for alias 'default'...
