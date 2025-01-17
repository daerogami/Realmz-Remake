const name : String = 'p_sp_regen.gd'
const menuname : String = 'SP Regeneration (P)'
const stacks : bool = false
const trait_types : Array = []
var chara
var power : int #in seconds, 1 round = 5s
var trait_source : String = ''


func _init(args : Array):
	#[chara, duration, permanent]
	chara = args[0]
	power = args[1]
	UI.ow_hud.creatureRect.logrect.log_other_text(chara, ' gets Regeneration !', null,'')


func get_saved_variables() :
	return [power]

func _on_new_round(_character : Creature) :
	if _character.used_resource=='SP' :
		chara.change_cur_sp(power)

func _on_time_pass(_character, seconds) :
	chara.change_cur_hp(power)
	if power <= 0 :
		chara.remove_trait(self)
	
func get_info_as_text() -> String :
	var usedpower : int = floor(sqrt(power*2))
	return 'Regenerating '+str(power)+'SP per round, Permanent'

