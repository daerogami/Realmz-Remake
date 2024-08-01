var name : String = 'Invisible Skin'
var attributes : Array = []
var tags : Array = ['Magical', 'Buff']
var schools : Array = ['Priest','Sorcerer']
var targettile : int = 1  #0=anywhere 1=creature 2=empty 3=nowall 
var level : int = 2
var selection_cost : int = 3
var max_plevel : int = 7
var in_field : bool = true
var in_combat : bool = true
var description : String = 'Makes the wearing of the magical skin invisible. Invisible creatures can move away from enemies during combat without the penalty of being attacked.'
var resist : int = 0 #ignores resistances and dodge
#var aoe : String = 'b1'
var los : bool = true
var ray : bool = false
var rot : bool = false
var proj_tex : String = 'Ball'
var proj_hit : String = 'Sphere'
var sounds : Array = ['spell launch 5.wav','identify.wav']
var max_focus_loss : int = 0

static func get_targets(_power : int, __casterchar)->int :
	return 1

static func get_min_duration(_power : int, __casterchar) -> int :
	return _power * 20

static func get_max_duration(_power : int, __casterchar) -> int :
	return _power * 50

static func get_range(_power : int, __casterchar) -> int :
	return 6
	
static func get_min_damage(_power:int, _casterchar) :
	return 0
	
static func get_max_damage(_power:int, _casterchar) :
	return 0
	
static func get_damage_roll(_power : int, _casterchar) :
	return 0

static func get_accuracy(_casterchar, _power : int) :
	return -7777777 #= infinite wiith resist==0 anyway

static func get_sp_cost(_power : int, _casterchar) :
	return 5*_power

static func get_target_number(_power : int, _casterchar) :
	return 1

static func get_aoe(_power : int, _casterchar) :
	return 'b1' #self

static func add_traits_to_target(_castercrea, c,_power) :
	var duration = 0
	for i in range(_power) :
		duration += 20 + randi()% 31
	var traitscript = load('res://shared_assets/traits/'+'t_invisible.gd')
	c.add_trait(traitscript,[duration])
