default current_mood_key = "a"
default mood_hud_expanded = False

default mood_profiles = {
    "a": {
        "name": "李宝瓶",
        "score": 50,
        "detail": "惦记着小师叔。",
    },
    "cpa": {
        "name": "陈平安",
        "score": 50,
        "detail": "仍在观察局势。",
    },
    "gucan": {
        "name": "顾璨",
        "score": 35,
        "detail": "还不愿意低头。",
    },
    "peiqian": {
        "name": "裴钱",
        "score": 60,
        "detail": "看什么都新鲜。",
    },
}

init python:
    config.overlay_screens.append("mood_hud")

    mood_event_delta = {
        "separation": -8,
        "reunion": 10,
        "comfort": 6,
        "pressure": -6,
        "doubt": -5,
        "resolve": 8,
        "truth": 5,
        "hurt": -10,
        "forgiveness": 12,
    }

    mood_choice_delta = {
        "listen": 6,
        "question": -3,
        "comfort": 8,
        "press": -6,
        "trust": 7,
        "doubt": -5,
        "protect": 5,
        "leave": -4,
    }

    def clamp_mood_score(value):
        return max(0, min(100, int(value)))

    def mood_state_label(value):
        score = clamp_mood_score(value)

        if score < 25:
            return "压抑"
        if score < 45:
            return "沉重"
        if score < 60:
            return "平静"
        if score < 75:
            return "坚定"

        return "释然"

    def adjust_mood(character_key, delta, detail=None):
        profile = mood_profiles.get(character_key, {
            "name": character_key,
            "score": 50,
            "detail": "",
        })

        old_score = clamp_mood_score(profile.get("score", 50))
        new_score = clamp_mood_score(old_score + delta)

        profile["score"] = new_score
        if detail is not None:
            profile["detail"] = detail

        mood_profiles[character_key] = profile

        store.current_mood_key = character_key
        renpy.restart_interaction()

    def story_mood_event(character_key, event_key):
        adjust_mood(character_key, mood_event_delta.get(event_key, 0))

    def story_mood_choice(character_key, choice_key):
        adjust_mood(character_key, mood_choice_delta.get(choice_key, 0))

    def set_mood(character_key, score, detail=None):
        profile = mood_profiles.get(character_key, {
            "name": character_key,
            "score": 50,
            "detail": "",
        })

        old_score = clamp_mood_score(profile.get("score", 50))
        new_score = clamp_mood_score(score)

        profile["score"] = new_score
        if detail is not None:
            profile["detail"] = detail

        mood_profiles[character_key] = profile

        store.current_mood_key = character_key
        renpy.restart_interaction()

    def change_mood(character_key, state, detail=None):
        delta_map = {
            "平静": 0,
            "不安": -8,
            "沉重": -10,
            "疲惫": -12,
            "动摇": -10,
            "愧疚": -8,
            "安心": 8,
            "坚定": 10,
            "释然": 12,
            "活泛": 6,
            "嘴硬": -4,
        }
        adjust_mood(character_key, delta_map.get(state, 0), detail)

screen mood_bar(value, width=170, height=12):
    fixed:
        xsize width
        ysize height

        add Solid("#332c25"):
            xsize width
            ysize height

        add Solid("#c9a061"):
            xsize int(width * value / 100.0)
            ysize height

screen mood_hud():
    zorder 140

    if not main_menu:
        $ profile = mood_profiles.get(current_mood_key, {"score": 50})
        $ score = profile.get("score", 50)
        $ state_text = mood_state_label(score)

        frame:
            xalign 0.985
            yalign 0.018
            xmaximum 260
            padding (8, 6)
            background Solid("#15120f9c")

            button:
                action ShowMenu("mood_status")
                hovered SetVariable("mood_hud_expanded", True)
                unhovered SetVariable("mood_hud_expanded", False)
                background None
                hover_background Solid("#c9a06118")
                padding (8, 3)

                if mood_hud_expanded:
                    hbox:
                        spacing 10
                        yalign 0.5

                        text "心境":
                            size 20
                            color "#eadfce"
                            font gui.interface_text_font

                        use mood_bar(score, 92, 8)

                        text "[state_text]":
                            size 20
                            color "#d5b174"
                            font gui.interface_text_font
                else:
                    text "心境  [state_text]":
                        size 19
                        color "#d8ccba"
                        font gui.interface_text_font

screen mood_status():
    tag menu

    use game_menu(_("心境"), scroll="viewport"):

        vbox:
            spacing 20

            text "角色心境值":
                size 42
                color "#ffffff"
                font gui.interface_text_font

            text "数值越高，表示角色越稳定、放松或坚定；数值越低，表示越疲惫、动摇或压抑。":
                size 26
                color "#c9d3dd"
                font gui.interface_text_font

            null height 8

            for key in sorted(mood_profiles.keys()):
                $ profile = mood_profiles[key]
                $ score = profile.get("score", 50)

                frame:
                    xfill True
                    padding (22, 16)
                    background Solid("#0f1724bb")

                    vbox:
                        spacing 8

                        hbox:
                            spacing 18
                            text profile.get("name", key):
                                size 32
                                color "#ffffff"
                                font gui.interface_text_font
                            text "[score]/100":
                                size 32
                                color "#ffd36a"
                                font gui.interface_text_font

                        use mood_bar(score, 520, 14)
