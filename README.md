# fmOptimizer
Ultimate Minecraft 1.8.9 PVP Optimizer

## Fm Optimizer 
全称"Fool me Optimizer", 一款专门为国人打造的Hypixel pvp优化器.
适配绝大部分游戏模式, 为您提供专业可靠, 安全开源的优化方案, 下载即用.
请通过release页面下载最新版本. 

--- 
## Third-Party Dependency

This project uses the terminal animation provided by
[ASCII_Rickroll](https://github.com/johnsoupir/ASCII_Rickroll), created by
[johnsoupir](https://github.com/johnsoupir).

The ASCII Rickroll library is not included directly in this repository. It must
be installed separately before running fmOptimizer.

### Installing ASCII_Rickroll

Clone the upstream repository:

```bash
git clone https://github.com/johnsoupir/ASCII_Rickroll.git
```

Enter its Python directory:

```bash
cd ASCII_Rickroll/Python
```

Install it into your current Python environment:

#### Windows

```powershell
py -m pip install .
```

fmOptimizer imports the library using:

```python
from ascii_rickroll import rickroll
```

The terminal animation is then played with:

```python
rickroll()
```

All credit for the ASCII Rickroll animation and frame data belongs to the
original project and its author. Please refer to the upstream repository for
its source code and usage information.
