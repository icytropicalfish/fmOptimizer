import os
import sys
import time
import webbrowser
import random


SUMO_TUTORIAL_URL = (
    "https://www.bilibili.com/video/BV1dkwzeeEDg/"
    "?share_source=copy_web&vd_source=9aaaf66120b154a6b6a64bed15db944d"
)

HITSELECT_TUTORIAL_URL = (
    "https://www.bilibili.com/video/BV1BrJSzTEXR/"
    "?share_source=copy_web&vd_source=9aaaf66120b154a6b6a64bed15db944d"
)

GITHUB_URL = "https://github.com/icytropicalfish/fmOptimizer"


YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"
RESET = "\033[0m"



def initialize_console():
    if os.name == "nt":
        os.system("")
        os.system("title FM Minecraft PvP Optimizer")

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(f"\n{GRAY}按 Enter 返回主菜单...{RESET}")


def loading(message="Loading"):
    duration = random.randint(10, 30)
    start_time = time.monotonic()
    animation = ["", ".", "..", "..."]
    frame = 0
    print("\033[?25l", end="", flush=True)

    try:
        while True:
            elapsed = time.monotonic() - start_time

            if elapsed >= duration:
                break

            percentage = min(
                int((elapsed / duration) * 100),
                99
            )

            dots = animation[frame % len(animation)]

            print(
                f"\r{YELLOW}{message}{dots:<3} "
                f"[{percentage:3d}%]{RESET}",
                end="",
                flush=True
            )

            frame += 1
            time.sleep(0.35)

        print(
            f"\r{GREEN}{message}... [100%]{RESET}"
            + " " * 10
        )

        time.sleep(random.randint(1, 5))

    finally:
        print("\033[?25h", end="", flush=True)


def open_url(url):
    try:
        opened = webbrowser.open_new_tab(url)

        if not opened:
            print(
                f"\n{RED}无法自动打开浏览器. {RESET}\n"
                f"请手动访问：{url}"
            )

    except webbrowser.Error:
        print(
            f"\n{RED}无法调用默认浏览器. {RESET}\n"
            f"请手动访问：{url}"
        )

def play_terminal_rickroll():
    try:
        from ascii_rickroll import rickroll

    except ImportError:
        clear_console()

        print(
            f"{RED}"
            "无法导入 ascii_rickroll. "
            f"{RESET}"
        )

        print(
            "\n请确认 ascii_rickroll 已安装到"
            "当前正在运行 main.py 的 Python 环境中. "
        )

        return False

    try:
        rickroll()
        return True

    except KeyboardInterrupt:
        return True

    except Exception as error:
        clear_console()

        print(
            f"{RED}"
            "ASCII Rick Roll 播放失败. "
            f"{RESET}"
        )

        print(
            f"\n错误类型：{type(error).__name__}"
            f"\n错误信息：{error}"
        )

        return False



def print_banner():
    print(
        YELLOW
        + "=========================================================================="
    )
    print(
        "                    Fool Me PVP OPTIMIZER"
    )
    print(
        "                         Arodios EDITION"
    )
    print(
        "=========================================================================="
        + RESET
    )
    print(
        f"{GRAY}"
        "本程序没有任何 hook/注入行为以及对游戏的修改行为. \n 一切优化均不通过修改游戏Qos/TCP(netsh/registery)以获得效用. \n 除Less KB以外在一切RBW服务器中允许使用，\n 没有在职官方RBW服务器管理正在使用本优化器. "
        f"{RESET}"
    )
    
    print(
        f"{GRAY}"
        "  fool me once, shame on me. fool me twice, shame on you"
        f"{RESET}"
    )

    print()


def show_main_menu():
    clear_console()
    print_banner()

    print(f"  {YELLOW}[1]{RESET}  Best KB")
    print(f"  {YELLOW}[2]{RESET}  Best Reg")
    print(f"  {YELLOW}[3]{RESET}  Less KB")
    print(f"  {YELLOW}[4]{RESET}  Reset to Default")
    print()
    print(f"  {YELLOW}[0]{RESET}  Exit")

def best_kb():
    clear_console()
    print_banner()
    loading("Loading Best KB profile")
    clear_console()
    print_banner()

    print(
        f"{YELLOW}检测到您的主要性能瓶颈："
        f"{WHITE}技术{RESET}"
    )

    print(
        "\n系统已找到以下有效的 KB 优化方案：\n"
    )

    print(
        f"  {YELLOW}[1]{RESET} "
        "[crracky] 你唯一需要的 SUMO 教程"
    )

    print(
        f"  {YELLOW}[2]{RESET} "
        "[kryptoke] 世界第二起床战争玩家教你 Hit Select"
    )

    print(
        f"  {YELLOW}[0]{RESET} "
        "返回主菜单"
    )

    while True:
        choice = input(
            f"\n{YELLOW}请选择优化方案 > {RESET}"
        ).strip()

        if choice == "1":
            print(
                f"\n{GREEN}"
                "正在打开 KB 优化方案1..."
                f"{RESET}"
            )

            time.sleep(0.8)
            open_url(SUMO_TUTORIAL_URL)
            pause()
            return

        if choice == "2":
            print(
                f"\n{GREEN}"
                "正在打开 KB 优化方案2..."
                f"{RESET}"
            )

            time.sleep(0.8)
            open_url(HITSELECT_TUTORIAL_URL)
            pause()
            return

        if choice == "0":
            return

        print(
            f"{RED}无效指令，请输入 0, 1 或 2. {RESET}"
        )

def best_reg():
    clear_console()
    print_banner()

    loading("Loading Best Reg profile")

    clear_console()

    play_terminal_rickroll()

    clear_console()
    print_banner()

    print(
        f"{RED}"
        "抱歉，优化器无法解决物理距离造成的 Hitreg 问题. "
        f"{RESET}"
    )

    print(
        "\n请尝试更改您的地球 Online地区设置，"
        "或者购买加速器. "
    )

    print(
        f"\n{GRAY}"
        "Registry changes applied: 0"
        f"{RESET}"
    )

    pause()

def less_kb():
    clear_console()
    print_banner()

    loading("Loading Less KB profile")

    clear_console()
    print_banner()

    print(
        f"{RED}"
        "Optimization failed."
        f"{RESET}"
    )

    print(
        "\n如果你想通过外部软件直接减少自己受到的 KB，"
        "\n而不是通过走位, 疾跑重置或操作技术，"
        "\n那么只有作弊这一种途径. "
    )

    print(
        f"\n检测到兼容解决方案："
        f"{YELLOW}vape.gg{RESET}"
    )

    print(
        f"\n{GRAY}"
        "该配置属于作弊功能，本优化器拒绝执行. "
        f"{RESET}"
    )

    pause()

def reset_to_default():
    clear_console()
    print_banner()

    loading("Restoring default configuration")

    clear_console()
    print_banner()

    print(
        f"{GREEN}"
        "明智的选择. "
        f"{RESET}"
    )

    print(
        f"\n检测到用户智商："
        f"{YELLOW}280{RESET}"
    )

    print(
        "\n所有优化配置均已恢复至默认状态. "
    )

    print(
        f"\n{GRAY}"
        "Restored settings: 0"
        "\n本程序从未修改任何注册表、网络或游戏设置. "
        f"{RESET}"
    )

    print(
        "\n如果该优化器对你有帮助，"
        "请在 GitHub 上给我点一个 Star. "
    )

    if "yourname/yourrepo" in GITHUB_URL:
        print(
            f"\n{GRAY}"
            "GitHub 仓库地址尚未配置. "
            f"{RESET}"
        )

        pause()
        return

    choice = input(
        f"\n{YELLOW}"
        "是否打开 GitHub 仓库？[Y/N] > "
        f"{RESET}"
    ).strip().lower()

    if choice in ("y", "yes"):
        open_url(GITHUB_URL)

    pause()

def main():
    initialize_console()

    while True:
        show_main_menu()

        choice = input(
            f"\n{YELLOW}请输入数字指令 > {RESET}"
        ).strip()

        if choice == "1":
            best_kb()

        elif choice == "2":
            best_reg()

        elif choice == "3":
            less_kb()

        elif choice == "4":
            reset_to_default()

        elif choice == "0":
            clear_console()

            print(
                f"{GREEN}"
                "Minecraft PvP Optimizer closed successfully."
                f"{RESET}"
            )

            time.sleep(0.8)
            break

        else:
            print(
                f"\n{RED}"
                f"未知指令：{choice}"
                f"{RESET}"
            )

            time.sleep(1.0)


if __name__ == "__main__":
    try:
        main()

    except (KeyboardInterrupt, EOFError):
        clear_console()

        print(
            f"{GREEN}"
            "Minecraft PvP Optimizer closed."
            f"{RESET}"
        )
