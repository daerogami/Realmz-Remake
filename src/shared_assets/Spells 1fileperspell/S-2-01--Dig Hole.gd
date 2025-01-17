var name : String = 'Dig Hole'
var attributes : Array = []
var tags : Array = ['Magical', 'Special Encounter', 'Dig Hole']
var schools : Array = ['Priest', 'Enchanter','Sorcerer']

var targettile : int = 0  #0=anywhere 1=creature 2=empty 3=nowall 

var level : int = 2
var selection_cost : int = 3
var max_plevel : int = 1
var in_field : bool = false
var in_combat : bool = false
var description : String = 'Allows the Party to dig a hole by magical means.\\nSP cost : 20'
var resist : int = 0 #ignores resistances and dodge
var los : bool = true
var ray : bool = false
var rot : bool = false
var proj_tex : String = 'Target'
var proj_hit : String = 'Target'
var sounds : Array = ['cloth armor.wav','cloth armor.wav']
var max_focus_loss : int = 0

static func get_targets(_power : int, __casterchar)->int :
	return 0

#static func get_hits(_power : int, __casterchar)->int :
#	return 1

static func get_min_duration(_power : int, __casterchar) -> int :
	return 0

static func get_max_duration(_power : int, __casterchar) -> int :
	return 0

#static func get_duration_roll(_power : int, __casterchar) -> int :
#	return 0

static func get_range(_power : int, __casterchar) -> int :
	return 0
	
static func get_min_damage(_power:int, _casterchar) :
	return 0
	
static func get_max_damage(_power:int, _casterchar) :
	return 0
	
static func get_damage_roll(_power : int, _casterchar) :
	return 0

static func get_accuracy(_casterchar, _power : int) :
	return 100 #= infinite wiith resist==0 anyway

static func get_sp_cost(_power : int, _casterchar) :
	return 20

static func get_target_number(_power : int, _casterchar) :
	return 0

static func get_aoe(_power : int, _casterchar) :
	return 'sf'
