
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftADDSUBleftMULDIVADD BEC DIV DO ELSE END EQ GEQ GRTR ID IF LEQ LESS LPAR MUL NEQ NUM READ RPAR SEM SUB THEN WHILE WRITEProgram : StatementsStatements : StatementStatements : Statements SEM StatementStatement : If\n                 | While\n                 | Read\n                 | Write\n                 | AssignmentIf : IF Comparison THEN Statements END \n          | IF Comparison THEN Statements ELSE Statements ENDWhile : WHILE Comparison DO Statements ENDWrite : WRITE ExpressionRead : READ IdAssignment : Id BEC ExpressionComparison : Expression Relation ExpressionRelation : EQ\n                | NEQ\n                | LESS\n                | LEQ\n                | GRTR\n                | GEQExpression : Expression ADD Expression\n                  | Expression SUB Expression\n                  | Expression MUL Expression\n                  | Expression DIV ExpressionExpression : LPAR Expression RPARExpression : NUMExpression : IdId : ID'
    
_lr_action_items = {'IF':([0,15,26,39,50,],[9,9,9,9,9,]),'WHILE':([0,15,26,39,50,],[10,10,10,10,10,]),'READ':([0,15,26,39,50,],[11,11,11,11,11,]),'WRITE':([0,15,26,39,50,],[13,13,13,13,13,]),'ID':([0,9,10,11,13,15,18,23,26,27,28,29,30,31,32,33,34,35,36,37,39,50,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,-16,-17,-18,-19,-20,-21,14,14,]),'$end':([1,2,3,4,5,6,7,8,14,19,20,22,24,25,40,43,44,45,46,47,49,51,53,],[0,-1,-2,-4,-5,-6,-7,-8,-29,-27,-28,-13,-12,-3,-14,-22,-23,-24,-25,-26,-9,-11,-10,]),'SEM':([2,3,4,5,6,7,8,14,19,20,22,24,25,40,41,43,44,45,46,47,48,49,51,52,53,],[15,-2,-4,-5,-6,-7,-8,-29,-27,-28,-13,-12,-3,-14,15,-22,-23,-24,-25,-26,15,-9,-11,15,-10,]),'END':([3,4,5,6,7,8,14,19,20,22,24,25,40,41,43,44,45,46,47,48,49,51,52,53,],[-2,-4,-5,-6,-7,-8,-29,-27,-28,-13,-12,-3,-14,49,-22,-23,-24,-25,-26,51,-9,-11,53,-10,]),'ELSE':([3,4,5,6,7,8,14,19,20,22,24,25,40,41,43,44,45,46,47,49,51,53,],[-2,-4,-5,-6,-7,-8,-29,-27,-28,-13,-12,-3,-14,50,-22,-23,-24,-25,-26,-9,-11,-10,]),'LPAR':([9,10,13,18,23,27,28,29,30,31,32,33,34,35,36,37,],[18,18,18,18,18,18,18,18,18,18,-16,-17,-18,-19,-20,-21,]),'NUM':([9,10,13,18,23,27,28,29,30,31,32,33,34,35,36,37,],[19,19,19,19,19,19,19,19,19,19,-16,-17,-18,-19,-20,-21,]),'BEC':([12,14,],[23,-29,]),'ADD':([14,17,19,20,24,38,40,42,43,44,45,46,47,],[-29,28,-27,-28,28,28,28,28,-22,-23,-24,-25,-26,]),'SUB':([14,17,19,20,24,38,40,42,43,44,45,46,47,],[-29,29,-27,-28,29,29,29,29,-22,-23,-24,-25,-26,]),'MUL':([14,17,19,20,24,38,40,42,43,44,45,46,47,],[-29,30,-27,-28,30,30,30,30,30,30,-24,-25,-26,]),'DIV':([14,17,19,20,24,38,40,42,43,44,45,46,47,],[-29,31,-27,-28,31,31,31,31,31,31,-24,-25,-26,]),'EQ':([14,17,19,20,43,44,45,46,47,],[-29,32,-27,-28,-22,-23,-24,-25,-26,]),'NEQ':([14,17,19,20,43,44,45,46,47,],[-29,33,-27,-28,-22,-23,-24,-25,-26,]),'LESS':([14,17,19,20,43,44,45,46,47,],[-29,34,-27,-28,-22,-23,-24,-25,-26,]),'LEQ':([14,17,19,20,43,44,45,46,47,],[-29,35,-27,-28,-22,-23,-24,-25,-26,]),'GRTR':([14,17,19,20,43,44,45,46,47,],[-29,36,-27,-28,-22,-23,-24,-25,-26,]),'GEQ':([14,17,19,20,43,44,45,46,47,],[-29,37,-27,-28,-22,-23,-24,-25,-26,]),'RPAR':([14,19,20,38,43,44,45,46,47,],[-29,-27,-28,47,-22,-23,-24,-25,-26,]),'THEN':([14,16,19,20,42,43,44,45,46,47,],[-29,26,-27,-28,-15,-22,-23,-24,-25,-26,]),'DO':([14,19,20,21,42,43,44,45,46,47,],[-29,-27,-28,39,-15,-22,-23,-24,-25,-26,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'Statements':([0,26,39,50,],[2,41,48,52,]),'Statement':([0,15,26,39,50,],[3,25,3,3,3,]),'If':([0,15,26,39,50,],[4,4,4,4,4,]),'While':([0,15,26,39,50,],[5,5,5,5,5,]),'Read':([0,15,26,39,50,],[6,6,6,6,6,]),'Write':([0,15,26,39,50,],[7,7,7,7,7,]),'Assignment':([0,15,26,39,50,],[8,8,8,8,8,]),'Id':([0,9,10,11,13,15,18,23,26,27,28,29,30,31,39,50,],[12,20,20,22,20,12,20,20,12,20,20,20,20,20,12,12,]),'Comparison':([9,10,],[16,21,]),'Expression':([9,10,13,18,23,27,28,29,30,31,],[17,17,24,38,40,42,43,44,45,46,]),'Relation':([17,],[27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> Statements','Program',1,'p_program','PLY_compiler.py',454),
  ('Statements -> Statement','Statements',1,'p_statements_statement','PLY_compiler.py',458),
  ('Statements -> Statements SEM Statement','Statements',3,'p_statements_statements','PLY_compiler.py',462),
  ('Statement -> If','Statement',1,'p_statement','PLY_compiler.py',468),
  ('Statement -> While','Statement',1,'p_statement','PLY_compiler.py',469),
  ('Statement -> Read','Statement',1,'p_statement','PLY_compiler.py',470),
  ('Statement -> Write','Statement',1,'p_statement','PLY_compiler.py',471),
  ('Statement -> Assignment','Statement',1,'p_statement','PLY_compiler.py',472),
  ('If -> IF Comparison THEN Statements END','If',5,'p_if','PLY_compiler.py',476),
  ('If -> IF Comparison THEN Statements ELSE Statements END','If',7,'p_if','PLY_compiler.py',477),
  ('While -> WHILE Comparison DO Statements END','While',5,'p_while','PLY_compiler.py',484),
  ('Write -> WRITE Expression','Write',2,'p_write','PLY_compiler.py',488),
  ('Read -> READ Id','Read',2,'p_read','PLY_compiler.py',492),
  ('Assignment -> Id BEC Expression','Assignment',3,'p_assignment','PLY_compiler.py',496),
  ('Comparison -> Expression Relation Expression','Comparison',3,'p_comparison','PLY_compiler.py',500),
  ('Relation -> EQ','Relation',1,'p_relation','PLY_compiler.py',504),
  ('Relation -> NEQ','Relation',1,'p_relation','PLY_compiler.py',505),
  ('Relation -> LESS','Relation',1,'p_relation','PLY_compiler.py',506),
  ('Relation -> LEQ','Relation',1,'p_relation','PLY_compiler.py',507),
  ('Relation -> GRTR','Relation',1,'p_relation','PLY_compiler.py',508),
  ('Relation -> GEQ','Relation',1,'p_relation','PLY_compiler.py',509),
  ('Expression -> Expression ADD Expression','Expression',3,'p_expression_binary','PLY_compiler.py',513),
  ('Expression -> Expression SUB Expression','Expression',3,'p_expression_binary','PLY_compiler.py',514),
  ('Expression -> Expression MUL Expression','Expression',3,'p_expression_binary','PLY_compiler.py',515),
  ('Expression -> Expression DIV Expression','Expression',3,'p_expression_binary','PLY_compiler.py',516),
  ('Expression -> LPAR Expression RPAR','Expression',3,'p_expression_parenthesis','PLY_compiler.py',520),
  ('Expression -> NUM','Expression',1,'p_expression_num','PLY_compiler.py',524),
  ('Expression -> Id','Expression',1,'p_expression_id','PLY_compiler.py',528),
  ('Id -> ID','Id',1,'p_id','PLY_compiler.py',532),
]
