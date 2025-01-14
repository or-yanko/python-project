from emoji import emojize
from time import sleep
import requests
from bs4 import BeautifulSoup as bs

def get_emoji_data():
	session = requests.Session()
	session.headers['User-Agent'] =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
	html = session.get('https://carpedm20.github.io/emoji/')

	# create a soup
	soup = bs(html.text, 'html.parser')
	emoji_list = []
	for row in soup.findAll('table')[0].findAll('tr')[2:-1]:
		entry = ':' + row.text.split(':')[1] + ':'
		emoji_list.append(entry)
	return emoji_list

all_emojis = get_emoji_data()
unsupported_emojis = [':dotted_line_face:', ':face_with_diagonal_mouth:',':nest_with_eggs:',':face_with_open_eyes_and_hand_over_mouth:',':heavy_equals_sign:',':face_with_peeking_eye:',':hand_with_index_finger_and_thumb_crossed:',':hand_with_index_finger_and_thumb_crossed_dark_skin_tone:',':hand_with_index_finger_and_thumb_crossed_light_skin_tone:','	:hand_with_index_finger_and_thumb_crossed_medium-dark_skin_tone:','	:hand_with_index_finger_and_thumb_crossed_medium-light_skin_tone:',':hand_with_index_finger_and_thumb_crossed_medium_skin_tone:',':handshake_dark_skin_tone_light_skin_tone:',':handshake_dark_skin_tone_medium-dark_skin_tone:',':handshake_dark_skin_tone_medium-light_skin_tone:',':handshake_dark_skin_tone_medium_skin_tone:',':handshake_light_skin_tone_dark_skin_tone:',':handshake_light_skin_tone_medium-dark_skin_tone:',':handshake_light_skin_tone_medium-light_skin_tone:',':handshake_light_skin_tone_medium_skin_tone:',':handshake_medium-dark_skin_tone_dark_skin_tone:',':handshake_medium-dark_skin_tone_light_skin_tone:',':handshake_medium-dark_skin_tone_medium-light_skin_tone:',':handshake_medium-dark_skin_tone_medium_skin_tone:',':handshake_medium-light_skin_tone_dark_skin_tone:',':handshake_medium-light_skin_tone_light_skin_tone:',':handshake_medium-light_skin_tone_medium-dark_skin_tone:',':handshake_medium-light_skin_tone_medium_skin_tone:',':handshake_medium_skin_tone_dark_skin_tone:','	:handshake_medium_skin_tone_light_skin_tone:','	:handshake_medium_skin_tone_medium-dark_skin_tone:',':handshake_medium_skin_tone_medium-light_skin_tone:',':heart_hands:',':heart_hands_dark_skin_tone:',':heart_hands_light_skin_tone:',':heart_hands_medium-dark_skin_tone:',':heart_hands_medium-light_skin_tone:',':heart_hands_medium_skin_tone:',':identification_card:',':index_pointing_at_the_viewer:',':index_pointing_at_the_viewer_dark_skin_tone:',':index_pointing_at_the_viewer_light_skin_tone:',':index_pointing_at_the_viewer_medium-dark_skin_tone:',':index_pointing_at_the_viewer_medium-light_skin_tone:',':index_pointing_at_the_viewer_medium_skin_tone:',':jar:','	:keycap_#:',':keycap_*:',':keycap_0:',':keycap_1:',':keycap_2:',':keycap_3:',':keycap_4:',':keycap_5:',':keycap_6:',':keycap_7:',':keycap_8:',':keycap_9:',':leftwards_hand:',':leftwards_hand_dark_skin_tone:',':leftwards_hand_light_skin_tone:',':leftwards_hand_medium-dark_skin_tone:',':leftwards_hand_medium-light_skin_tone:',':leftwards_hand_medium_skin_tone:',':palm_down_hand:',':palm_down_hand_dark_skin_tone:',':palm_down_hand_light_skin_tone:',':palm_down_hand_medium-dark_skin_tone:',':palm_down_hand_medium-light_skin_tone:',':palm_down_hand_medium_skin_tone:',':palm_up_hand:',':palm_up_hand_dark_skin_tone:',':palm_up_hand_light_skin_tone:',':palm_up_hand_medium-dark_skin_tone:',':palm_up_hand_medium-light_skin_tone:',':palm_up_hand_medium_skin_tone:',':person_with_crown:',':person_with_crown_dark_skin_tone:',':person_with_crown_light_skin_tone:',':person_with_crown_medium-dark_skin_tone:',':person_with_crown_medium-light_skin_tone:',':person_with_crown_medium_skin_tone:',':pouring_liquid:',':pregnant_man:',':pregnant_man_dark_skin_tone:',':pregnant_man_light_skin_tone:',':pregnant_man_medium-dark_skin_tone:',':pregnant_man_medium-light_skin_tone:',':pregnant_man_medium_skin_tone:',':pregnant_person:',':pregnant_person_dark_skin_tone:',':pregnant_person_light_skin_tone:',':pregnant_person_medium-dark_skin_tone:',':pregnant_person_medium-light_skin_tone:',':pregnant_person_medium_skin_tone:',':rightwards_hand:',':rightwards_hand_dark_skin_tone:',':rightwards_hand_light_skin_tone:',':rightwards_hand_medium-dark_skin_tone:',':rightwards_hand_medium-light_skin_tone:',':rightwards_hand_medium_skin_tone:',':ring_buoy:',':saluting_face:',':x-ray:',':playground_slide:',':melting_face:',':low_battery:',':handshake_medium_skin_tone_light_skin_tone:',':handshake_medium_skin_tone_medium-dark_skin_tone:',':hand_with_index_finger_and_thumb_crossed_medium-dark_skin_tone:',':hand_with_index_finger_and_thumb_crossed_medium-light_skin_tone:',':hamsa:',':face_holding_back_tears:',':biting_lip:']

for emoji in all_emojis:
	if emoji not in unsupported_emojis:
		print(emojize(emoji), end = '')
		sleep(0.02)
