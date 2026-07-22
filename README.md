# whojay Skill

从本机 Codex 会话中蒸馏出的工程与学术双工作流 Skill。

它包含两个相互连接的部分：

- **Work**：工程诊断、实现、验证、Git 交付，以及研究定位、实验治理、证据到论文主张的完整流程。
- **Persona**：证据优先、边界严格、直接纠偏、验证导向和闭环交付的协作方式。

## 使用

在 Codex 中安装本仓库的根 Skill：

```text
请安装 https://github.com/WhoJay0609/whojay-skill
```

也可以手动安装：

```bash
git clone https://github.com/WhoJay0609/whojay-skill.git
mkdir -p ~/.codex/skills/colleague-whojay
cp whojay-skill/SKILL.md ~/.codex/skills/colleague-whojay/SKILL.md
```

然后在新任务中调用：

```text
$colleague-whojay 按照我的工作流处理这个任务
```

## 文件

- `SKILL.md`：Codex 可直接加载的 Work + Persona 合并入口
- `work.md` / `work_skill.md`：工程与学术工作流
- `persona.md` / `persona_skill.md`：协作和决策风格
- `meta.json` / `manifest.json`：dot-skill v3 元数据与清单

## 证据与隐私边界

该 Skill 来自去重、隐私过滤后的会话模式分析。仓库不包含原始会话、命令输出、凭据、会话 ID、私人标识符或本机绝对路径。没有可靠证据支持的公司、职位级别、性别、MBTI、学历层级及线下人际属性均保持未设置。

## License

MIT
