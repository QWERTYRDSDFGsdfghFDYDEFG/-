################################################################################
## 书简湖主菜单：分层微动背景
################################################################################

## 这套效果采用 Ren'Py 原生 Transform/ATL，不依赖 Cubism SDK。
## 底图保持完全静止；灯、暖光、湖雾和前景阴影分别作为独立 RGBA 层自行循环。


transform main_menu_base_live:
    xalign 0.5
    yalign 0.5
    xysize (1920, 1080)


transform main_menu_mist_live:
    subpixel True
    xalign 0.5
    yalign 0.5
    xysize (1920, 1080)
    alpha 0.045
    xoffset -18
    linear 16.0 xoffset 12 alpha 0.075
    linear 14.0 xoffset -18 alpha 0.045
    repeat


transform main_menu_shadow_live:
    subpixel True
    xalign 0.5
    yalign 0.5
    xysize (1920, 1080)
    alpha 0.12
    linear 5.0 alpha 0.16
    linear 6.5 alpha 0.12
    repeat


transform main_menu_warm_light_live:
    subpixel True
    xalign 0.5
    yalign 0.5
    xysize (1920, 1080)
    xoffset -112
    blend "add"
    alpha 0.075
    linear 0.18 alpha 0.115
    linear 0.12 alpha 0.085
    linear 0.36 alpha 0.13
    linear 0.72 alpha 0.095
    linear 1.20 alpha 0.075
    repeat


transform main_menu_lamp_glow_live:
    subpixel True
    xpos 1265
    ypos 830
    blend "add"
    alpha 0.055
    linear 0.16 alpha 0.09
    linear 0.12 alpha 0.065
    linear 0.42 alpha 0.11
    linear 0.72 alpha 0.07
    linear 1.10 alpha 0.055
    repeat


screen main_menu_live_background():
    fixed:
        xfill True
        yfill True

        add gui.main_menu_background at main_menu_base_live
        add "gui/main_menu_live/mist_v1.png" at main_menu_mist_live
        add "gui/main_menu_live/shadow_v1.png" at main_menu_shadow_live
        add "gui/main_menu_live/light_v1.png" at main_menu_warm_light_live
        add "gui/main_menu_live/glow_v1.png" at main_menu_lamp_glow_live
