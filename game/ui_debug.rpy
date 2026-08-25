label ui_debug_entry:
    jump ui_debug


## UI 调试场
##
## 仅供开发阶段检查现有对话框、选项和样式，不接入正式主线。
## VS Code 中选择“Ren'Py：打开 UI 调试场”即可直接进入。

default ui_debug_guides_visible = True


screen ui_debug_guides():
    zorder 200

    key "K_F8" action ToggleVariable("ui_debug_guides_visible")

    if ui_debug_guides_visible:
        add Solid("#d6a45a80") xpos 959 ypos 0 xsize 2 ysize 1080
        add Solid("#d6a45a80") xpos 0 ypos 539 xsize 1920 ysize 2

        # 5% 安全区参考线，便于发现贴边和不同容器的对齐偏差。
        add Solid("#8eb6c880") xpos 95 ypos 54 xsize 2 ysize 972
        add Solid("#8eb6c880") xpos 1823 ypos 54 xsize 2 ysize 972
        add Solid("#8eb6c880") xpos 95 ypos 53 xsize 1730 ysize 2
        add Solid("#8eb6c880") xpos 95 ypos 1025 xsize 1730 ysize 2

        frame:
            xalign 1.0
            yalign 0.0
            margin (18, 18)
            padding (14, 10)
            background "#11100ed9"

            vbox:
                spacing 4
                text "UI 调试场 · 1920×1080" size 22 color "#f0dfc6"
                text "F8 显示/隐藏参考线 · Shift+I 检查样式 · Shift+R 热重载" size 16 color "#c8b89f"


label ui_debug:
    $ clear_dialogue_pair()
    $ clear_dialogue_paralanguage()

    scene expression Solid("#25211c")
    show screen ui_debug_guides

    narrator "这里是开发专用 UI 调试场，不会进入正式剧情。"
    narrator "先按 Shift+I，再把鼠标放到文字、头像或文本框上，可以查看实际生效的样式与尺寸。"

    jump ui_debug_menu


label ui_debug_menu:
    menu:
        "运行完整对话测试":
            jump ui_debug_dialogue

        "检查长文本与换行":
            jump ui_debug_long_text

        "检查选项按钮":
            jump ui_debug_choices

        "切换参考线（F8）":
            $ ui_debug_guides_visible = not ui_debug_guides_visible
            jump ui_debug_menu

        "退出 UI 调试场":
            jump ui_debug_exit


label ui_debug_dialogue:
    a "普通角色对白：检查姓名、头像、正文颜色与文本框高度。"

    cpa "主角对白：检查陈平安主题、头像和强调色是否与普通角色明显区分。"

    narrator "旁白：检查浅色文本框、留白、最大行宽和阅读对比度。"

    cpa_thought "主角心声：检查无姓名状态、斜体正文和冷色主题。"

    inner_voice "普通心理活动：检查无姓名状态与较暗的内心主题。"

    $ set_dialogue_paralanguage("低声")
    peiqian "带副语言标签的对白：检查标签是否挤压正文或头像。"
    $ clear_dialogue_paralanguage()

    $ set_dialogue_pair("李宝瓶", "崔东山")
    a "双人对白左侧发言：检查当前说话人的高亮、姓名牌和头像位置。"
    cds "双人对白右侧发言：检查高亮切换后，两侧布局是否稳定。"
    $ clear_dialogue_pair()

    jump ui_debug_menu


label ui_debug_long_text:
    a "这是一段用于检查自动换行、行间距和文本安全区的较长对白。保存脚本后可以按 Shift+R 重新加载，再使用 Shift+I 查看 say_dialogue、上层 vbox 以及 window 最终采用的尺寸和样式属性。"

    narrator "这是一段较长旁白，用于观察浅色背景上的正文是否清晰，连续两到三行时是否仍然留有足够的上下边距，以及文字是否会越过画面中央参考线或贴近屏幕安全区。"

    jump ui_debug_menu


label ui_debug_choices:
    menu:
        "短选项":
            narrator "已选择短选项。"

        "这是一条用于检查长文本换行、左右内边距与悬停位移的选项":
            narrator "已选择长选项。"

        "检查第三个选项在纵向排列中的间距":
            narrator "已选择第三个选项。"

        "返回 UI 调试目录":
            pass

    jump ui_debug_menu


label ui_debug_exit:
    $ clear_dialogue_pair()
    $ clear_dialogue_paralanguage()
    hide screen ui_debug_guides
    return
