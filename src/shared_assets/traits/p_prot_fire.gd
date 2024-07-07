const name : String = 'p_prot_fire.gd'
const menuname : String = 'Fire Protection (P)'
const stacks : bool = false
const trait_types : Array = []
var chara
const permanent : int = 1
var trait_source : String = ''

func _init(args : Array):
	#[chara]
	chara = args[0]
	UI.ow_hud.creatureRect.logrect.log_other_text(chara, ' gets Permanent Fire Protection !', null,'')

func get_saved_variables() :
	return []

func _on_get_stat(statname : String, stat : int) :
	if statname == "MultiplierFire" :
		return stat*0.5  #1  stat = 1% chance
	else :
		return stat

func get_info_as_text() -> String :
	return 'Permanent Fire Protection'+' (source : '+trait_source+')'

func equals_args(traits_array : Array) :
	return true
