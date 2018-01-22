
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'B4539F131D3E6B76E690C5A06AB9D0AD'
    
_lr_action_items = {'COUT':([6,10,12,14,17,18,29,46,47,50,51,52,56,57,67,68,69,70,71,72,],[8,-8,8,-6,-7,-5,-9,-22,-23,-21,-18,-20,-19,-17,8,-24,-25,-26,8,8,]),'DEFAULT':([10,12,14,17,18,26,29,46,47,50,51,52,53,54,55,56,57,58,67,68,69,70,71,72,73,74,75,79,80,81,],[-8,-4,-6,-7,-5,-3,-9,-22,-23,-21,-18,-20,60,60,60,-19,-17,60,-4,-24,-25,-26,-4,-4,-33,-30,-29,-34,-32,-31,]),'CHARACTER':([25,32,59,],[34,41,65,]),'NUMBER':([25,27,38,59,],[35,37,49,66,]),'CHAR':([6,10,12,14,17,18,29,46,47,50,51,52,56,57,67,68,69,70,71,72,],[9,-8,9,-6,-7,-5,-9,-22,-23,-21,-18,-20,-19,-17,9,-24,-25,-26,9,9,]),'ARITHEMATIC':([15,48,],[27,27,]),'CASE':([10,12,14,17,18,26,29,46,47,50,51,52,53,54,55,56,57,58,67,68,69,70,71,72,73,74,75,79,80,81,],[-8,-4,-6,-7,-5,-3,-9,-22,-23,-21,-18,-20,59,59,59,-19,-17,59,-4,-24,-25,-26,-4,-4,-33,-30,-29,-34,-32,-31,]),'SEMI':([8,20,21,22,30,31,36,37,39,40,41,42,48,49,76,77,78,],[-12,-11,-10,29,-13,-15,46,47,-14,-16,51,52,56,57,79,80,81,]),'SWITCH':([6,10,12,14,17,18,29,46,47,50,51,52,56,57,67,68,69,70,71,72,],[11,-8,11,-6,-7,-5,-9,-22,-23,-21,-18,-20,-19,-17,11,-24,-25,-26,11,11,]),'COLON':([60,65,66,],[67,71,72,]),'R_CURLY':([6,7,10,12,14,17,18,26,29,46,47,50,51,52,53,54,55,56,57,58,61,62,63,64,67,68,69,70,71,72,73,74,75,79,80,81,],[13,19,-8,-4,-6,-7,-5,-3,-9,-22,-23,-21,-18,-20,-28,-28,-28,-19,-17,-28,68,69,70,-27,-4,-24,-25,-26,-4,-4,-33,-30,-29,-34,-32,-31,]),'ASSIGN':([24,28,],[32,38,]),'$end':([2,13,19,],[0,-1,-2,]),'STRING':([23,],[30,]),'L_CURLY':([5,43,44,45,],[6,53,54,55,]),'NAME':([6,9,10,12,14,16,17,18,23,25,27,29,32,38,46,47,50,51,52,56,57,67,68,69,70,71,72,],[15,24,-8,15,-6,28,-7,-5,31,33,36,-9,42,48,-22,-23,-21,-18,-20,-19,-17,15,-24,-25,-26,15,15,]),'INT':([0,6,10,12,14,17,18,29,46,47,50,51,52,56,57,67,68,69,70,71,72,],[1,16,-8,16,-6,-7,-5,-9,-22,-23,-21,-18,-20,-19,-17,16,-24,-25,-26,16,16,]),'L_BRACE':([3,11,],[4,25,]),'BREAK':([10,12,14,17,18,26,29,46,47,50,51,52,56,57,67,68,69,70,71,72,73,74,75,],[-8,-4,-6,-7,-5,-3,-9,-22,-23,-21,-18,-20,-19,-17,-4,-24,-25,-26,-4,-4,76,77,78,]),'R_BRACE':([4,33,34,35,],[5,43,44,45,]),'MAIN':([1,],[3,]),'OP':([8,30,31,],[23,39,40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function':([6,12,67,71,72,],[14,14,14,14,14,]),'case':([53,54,55,58,],[58,58,58,58,]),'statements':([6,12,67,71,72,],[7,26,73,74,75,]),'str':([8,],[20,]),'case_switch':([6,12,67,71,72,],[10,10,10,10,10,]),'program':([0,],[2,]),'statement':([6,12,67,71,72,],[12,12,12,12,12,]),'var':([8,],[21,]),'cases':([53,54,55,58,],[61,62,63,64,]),'modifier':([6,12,38,67,71,72,],[17,17,50,17,17,17,]),'expression':([6,12,67,71,72,],[18,18,18,18,18,]),'more':([8,],[22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> INT MAIN L_BRACE R_BRACE L_CURLY R_CURLY','program',6,'p_program','switch.py',121),
  ('program -> INT MAIN L_BRACE R_BRACE L_CURLY statements R_CURLY','program',7,'p_program','switch.py',122),
  ('statements -> statement statements','statements',2,'p_statements','switch.py',136),
  ('statements -> <empty>','statements',0,'p_statements_empty','switch.py',140),
  ('statement -> expression','statement',1,'p_statement','switch.py',144),
  ('statement -> function','statement',1,'p_statement','switch.py',145),
  ('statement -> modifier','statement',1,'p_statement','switch.py',146),
  ('statement -> case_switch','statement',1,'p_statement','switch.py',147),
  ('function -> COUT more SEMI','function',3,'p_function','switch.py',162),
  ('more -> var','more',1,'p_more','switch.py',170),
  ('more -> str','more',1,'p_more','switch.py',171),
  ('more -> <empty>','more',0,'p_nomore_func','switch.py',175),
  ('str -> OP STRING','str',2,'p_func_str','switch.py',179),
  ('str -> OP STRING OP','str',3,'p_func_str','switch.py',180),
  ('var -> OP NAME','var',2,'p_var','switch.py',185),
  ('var -> OP NAME OP','var',3,'p_var','switch.py',186),
  ('expression -> INT NAME ASSIGN NUMBER SEMI','expression',5,'p_expression','switch.py',193),
  ('expression -> CHAR NAME ASSIGN CHARACTER SEMI','expression',5,'p_expression','switch.py',194),
  ('expression -> INT NAME ASSIGN NAME SEMI','expression',5,'p_exp_name','switch.py',199),
  ('expression -> CHAR NAME ASSIGN NAME SEMI','expression',5,'p_exp_name','switch.py',200),
  ('expression -> INT NAME ASSIGN modifier','expression',4,'p_expression_m','switch.py',204),
  ('modifier -> NAME ARITHEMATIC NAME SEMI','modifier',4,'p_modifier','switch.py',208),
  ('modifier -> NAME ARITHEMATIC NUMBER SEMI','modifier',4,'p_modifier_n','switch.py',212),
  ('case_switch -> SWITCH L_BRACE NAME R_BRACE L_CURLY cases R_CURLY','case_switch',7,'p_case_switch','switch.py',220),
  ('case_switch -> SWITCH L_BRACE CHARACTER R_BRACE L_CURLY cases R_CURLY','case_switch',7,'p_case_switch_1','switch.py',224),
  ('case_switch -> SWITCH L_BRACE NUMBER R_BRACE L_CURLY cases R_CURLY','case_switch',7,'p_case_switch_2','switch.py',228),
  ('cases -> case cases','cases',2,'p_cases','switch.py',234),
  ('cases -> <empty>','cases',0,'p_cases_empty','switch.py',238),
  ('case -> CASE NUMBER COLON statements','case',4,'p_case','switch.py',243),
  ('case -> CASE CHARACTER COLON statements','case',4,'p_case','switch.py',244),
  ('case -> CASE NUMBER COLON statements BREAK SEMI','case',6,'p_case_break','switch.py',248),
  ('case -> CASE CHARACTER COLON statements BREAK SEMI','case',6,'p_case_break','switch.py',249),
  ('case -> DEFAULT COLON statements','case',3,'p_case_default','switch.py',265),
  ('case -> DEFAULT COLON statements BREAK SEMI','case',5,'p_case_bdefault','switch.py',270),
]