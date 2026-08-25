# 角色出图身份索引

用途：让 Codex 在收到“生成某角色图片 / 立绘 / 表情 / 动作图 / 场景图 / 演出图”请求时，先自动定位该角色必须阅读的参考文档，而不是依赖用户每次手动提醒。

本索引不是只管“脸部身份标准”，还同时管理：

- 角色专属身份标准文件
- 逐场分镜表
- Ren'Py 演出脚本执行表
- 通用立绘 / 构图规则

---

## 1. 默认工作流

当用户提出以下类型请求时，必须先查本索引：

- 生成角色图片
- 生成角色立绘
- 修改角色立绘
- 补角色表情 / 动作 / 场景版本
- 做某角色在某一场戏里的演出图
- 为 Ren'Py 某场戏补背景、补立绘、补构图参考

默认执行顺序：

1. 先按“角色名 / 别名 / 变量名”匹配本索引。
2. 先读该角色的“专属身份标准文件”。
3. 再读该角色关联的“逐场分镜表”。
4. 再读该角色关联的 “Ren'Py 演出脚本执行表”。
5. 如果该角色还没有专属身份标准，就先读通用规则文档，再结合分镜表和执行表出图。

如果用户只说简称、昵称或变量名，也要先尝试按“触发词 / 别名 / 变量名”匹配。

---

## 2. 全局必读文档

### 2.1 角色母版目录硬规则

- 本项目角色母版统一以 `lh/` 目录内文件为准。
- 进行锁脸、锁发型、锁服装的正式出图时，必须优先调用 `lh/角色目录/` 内的母版图与标准文档。
- 其他来源图片如果没有同步写入 `lh/` 并被标准文档明确登记，只能作为临时参考，不能替代角色母版。
- 双角色或多人剧情图，只要涉及“像不像母版”，默认都要先回查 `lh/`，再决定是否进入生成或编辑流程。

以下文档不区分角色，凡是做角色图、演出图、场景配套图，默认都应纳入参考：

- `Codex/character_generation_workflow.md`
- `Codex/character_asset_update_rules.md`
- `Codex/semi_to_cel_guide.md`（涉及半写实身份图转赛璐璐 / 动画风时额外必读）
- `角色立绘设计原则.md`
- `《剑来》VN演出与构图总手册.md`

以下文档按章节范围补充参考：

- 序章 / `script.rpy` 相关：
  - `script逐场分镜表.md`
  - `script_RenPy演出脚本执行表.md`
- Chapter 2 到 Chapter 5 相关：
  - `script_chapter2~5逐场分镜表.md`
  - `script_chapter2~5_RenPy演出脚本执行表.md`

---

## 3. 已有专属身份标准的角色

| 角色 | 触发词 / 别名 / 变量名 | 专属身份标准文件 | 关键母版 | 分镜 / 演出补充 |
| --- | --- | --- | --- | --- |
| 陈平安 | 陈平安、陈平、cpa | `lh/cpa/CPA_FACE_IDENTITY_STANDARD.md` | `lh/cpa/cpa_face_standard_01.png`、`lh/cpa/cpa_outfit_variant_06_warm_weather.png` | `script逐场分镜表.md`、`script_RenPy演出脚本执行表.md`、`script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` |
| 裴钱 | 裴钱、peiqian、pq | `lh/peiqian/PEIQIAN_FACE_IDENTITY_STANDARD.md` | `lh/peiqian/peiqian_master_v02.png` | `script逐场分镜表.md`、`script_RenPy演出脚本执行表.md`、`script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` |
| 李宝瓶 | 李宝瓶、宝瓶、lbp、a | `lh/lbp/李宝瓶固定脸部身份与当前服装标准.md` | `lh/lbp/lbp_face_close_v1.png`、`lh/lbp/lbp_face_34_v1.png`、`lh/lbp/lbp_exp_sheet_v1.png` | `script逐场分镜表.md`、`script_RenPy演出脚本执行表.md` |
| 崔东山 | 崔东山、cds | `lh/cds/cds_face_ref.md`（唯一主标准：固定脸部身份与当前服装） | 正面身份母版：`lh/cds/cds-v1.png`；三分之四侧母版：`lh/cds/cds_exp_34_v1.png`；同机位表情差分基底：`lh/cds/cds_face_34_cand_v1.png`；全身体型与当前服装母版：`lh/cds/cds_full_base_v11.png` | `script逐场分镜表.md`、`script_RenPy演出脚本执行表.md` |
| 李槐 | 李槐、lihuai、lh、c | `lh/lihuai/lh_face_ref.md` | 脸部与表情：`lh/lihuai/lh_expression_sheet_basic_v1.png`；全身服装与序-03动作：`lh/lihuai/lh_action_c1_03_white_deer_entry_v1.png`；序-05动作：`lh/lihuai/lh_action_c1_05_hero_entry_v1.png` | `script逐场分镜表.md`、`script_RenPy演出脚本执行表.md` |
| 朱敛 | 朱敛、zl、老厨子 | `lh/zl/zl_face_ref.md`；原文考据先读 `lh/zl/zl_text_evidence.md`；语义拓扑读 `lh/zl/zl_face_topology_v1.md`；规则变形网格读 `lh/zl/zl_face_grid_mesh_rules_v1.md` | 脸部母版：`lh/zl/exec-42da0fb1-b19a-4708-b3b4-2fc6f04516aa.png`；478点数据：`lh/zl/zl_face_mesh_v1.json`；规则网格：`lh/zl/zl_face_grid_mesh_v1.json`；网格检查图：`lh/zl/zl_face_grid_mesh_map_v1.png`；全身母版：`lh/zl/zl_full_base_v1.png` | `script逐场分镜表.md`、`script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` |

### 3.1 崔东山母版调用顺序

- 生成或修正脸部身份：先读 `lh/cds/cds_face_ref.md`，以 `lh/cds/cds-v1.png` 为最高优先级。
- 生成三分之四侧镜头：以 `lh/cds/cds_exp_34_v1.png` 锁定转角后的骨相与五官透视。
- 生成认真、疑惑、微笑、委屈、小得意等表情差分：以 `lh/cds/cds_face_34_cand_v1.png` 固定镜头、光线、角度和构图，只允许微调表情肌。
- 生成全身、服装或动作差分：以 `lh/cds/cds_full_base_v11.png` 固定体型、站姿、袍服层级、配色、腰带、垂绦和鞋履，同时用 `lh/cds/cds-v1.png` 回锁脸部身份。
- 若近景与全身图的脸部细节冲突，以近景身份母版为准；全身图不得反向覆盖近景脸部标准。

### 3.2 主菜单角色场景资产

| 资产 | 涉及角色 | 身份依据 | 状态 | 用途与限制 |
| --- | --- | --- | --- | --- |
| `gui/main_menu_shujianhu_v1.png` | 陈平安、顾璨、小泥鳅 | 陈平安依据 `lh/cpa/cpa_face_standard_01.png` 与 `lh/cpa/cpa_outfit_variant_06_warm_weather.png`；顾璨与小泥鳅暂无身份母版，仅使用不可辨认的远景背影与水纹 | 当前使用 | 主菜单“孤灯照账”背景；不是角色母版，不得反向覆盖陈平安身份标准，也不得作为顾璨或小泥鳅的人设依据 |
| `gui/main_menu_live/lamp_v1.png` | 无新增角色 | 基于“孤灯照账”构图生成的独立透明油灯层 | 停用 | 完整灯具与底图原灯无法精确重合，会产生玻璃罩和灯架重影；文件保留供回查，不再参与合成 |
| `gui/main_menu_live/flame_v1.png` | 无新增角色 | 依据底图油灯的火焰色温生成 | 停用 | 底图已有火苗，重复叠加会形成双火舌；文件保留，只有未来提供无火底图时才能重新启用 |
| `gui/main_menu_live/glow_v1.png` | 陈平安（仅受光区域） | 依据底图油灯位置生成的局部透明暖光 | 当前使用 | 只覆盖灯罩周围的小范围柔光，不包含灯具结构；与人物暖光层共同营造局部受光 |
| `gui/main_menu_live/light_v1.png` | 陈平安（仅受光区域） | 角色身份仍以陈平安既有母版为准；本图不包含角色像素 | 当前使用 | 透明暖光柔色层，用于人物面部、右袖、手部和桌面局部受光，不得作为角色母版 |
| `gui/main_menu_live/mist_v1.png` | 无 | 独立透明湖雾与水光气氛层 | 当前使用 | 仅用于主菜单极慢横向漂移，保持低透明度，不做仙侠粒子化处理 |
| `gui/main_menu_live/shadow_v1.png` | 无 | 独立透明前景阴影层 | 当前使用 | 用于压住桌下与画面边缘，保持克制，不遮挡导航与标题可读性 |

---

## 4. 已纳入索引、但暂无专属身份标准的角色

规则：以下角色如果收到出图请求，先读通用规则文档，再读本表指定的分镜 / 演出文档；若后续为该角色建立专属身份标准，必须立刻回填到本索引。

| 角色 | 触发词 / 变量名 | 当前优先参考 | 当前状态 |
| --- | --- | --- | --- |
| 茅小冬 | 茅小冬、k | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 吴懿 | 吴懿、wy | `script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` | 已纳入索引，待建立专属身份标准 |
| 董水井 | 董水井、donsujing | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 高煊 | 高煊、c1 | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 许弱 | 许弱、xuluo | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 阮秀 | 阮秀、rx | `script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` | 已纳入索引，待建立专属身份标准 |
| 徐小桥 | 徐小桥、xxq | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 绣花江水神 | 绣花江水神、xhjs | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 吴鸢 | 吴鸢、h1 | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 阮邛 | 阮邛、rq | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 崔瀺 | 崔瀺、cc | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 孙登先 | 孙登先、sdx | `script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` | 已纳入索引，待建立专属身份标准 |
| 金色儒衫小人儿 | 金色儒衫小人儿、jssr | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 顾韬 | 顾韬、gt | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 顾璨 | 顾璨、gc | `script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` | 已纳入索引，待建立专属身份标准 |
| 李牧玺 | 李牧玺、lmx | `script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` | 已纳入索引，待建立专属身份标准 |
| 宋郎中 | 宋郎中、slz | `script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` | 已纳入索引，待建立专属身份标准 |
| 老掌柜 | 老掌柜、lzg | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 田湖君 | 田湖君、thj | `script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` | 已纳入索引，待建立专属身份标准 |
| 杨老头 | 杨老头、ylt | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 范彦 | 范彦、fy | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 吕采桑 | 吕采桑、lcs | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 元袁 | 元袁、yy | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 小泥鳅 | 小泥鳅、xnq | `script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` | 已纳入索引，待建立专属身份标准 |
| 中年男人 | 中年男人、znr | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |
| 顾氏 | 顾氏、gs | `script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md` | 已纳入索引，待建立专属身份标准 |
| 文圣 | 文圣、ws | `角色立绘设计原则.md`、`《剑来》VN演出与构图总手册.md` | 已纳入索引，待补场次级参考与专属身份标准 |

---

## 5. 额外补充：分镜表 / 演出表的使用口径

如果用户不是单纯说“画一个角色”，而是说：

- “给我补某场戏的图”
- “把这个角色放进某一段剧情场景里”
- “补 Ren'Py 能直接落地的演出图”

那么除了查角色，还必须同时按章节查这些文档：

- 序章相关：`script逐场分镜表.md` + `script_RenPy演出脚本执行表.md`
- Chapter 2 到 Chapter 5 相关：`script_chapter2~5逐场分镜表.md` + `script_chapter2~5_RenPy演出脚本执行表.md`

结论：角色身份标准负责“这个人是谁”，分镜表和执行表负责“这个人在哪一场、以什么构图和演出口径出现”。

---

## 6. 维护规则

- 新增一个角色身份标准后，必须同步把该角色补进“已有专属身份标准的角色”。
- 新增新的逐场分镜表或新的 Ren'Py 演出脚本执行表后，也必须同步更新本索引。
- 若角色标准文件路径变动，必须先更新本索引，再继续出图工作。
- 若一个角色后续拆分出“脸部母版标准”和“服装母版标准”，也要在本索引里一起写明。
- 若某角色已在 `characters.rpy` 中定义，但仍没有专属身份标准，收到该角色高频出图请求时，应优先建议补建该角色标准文件。
