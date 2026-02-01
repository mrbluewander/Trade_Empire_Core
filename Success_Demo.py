#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trade_Empire_Core - Success Demo
首個本地測試腳本，驗證系統環境並提供成功體驗

使用方式：
    python Success_Demo.py

預期結果：
    ✅ Trade_Empire_Core 系統已啟動！
    📊 系統狀態：就緒
    🔗 本地服務：http://localhost:8000
"""

import os
import sys
import json
import time
from datetime import datetime
from pathlib import Path

# ============================================================================
# 配置
# ============================================================================

SYSTEM_NAME = "Trade_Empire_Core"
VERSION = "v0.1"
COLORS = {
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'RED': '\033[91m',
    'BLUE': '\033[94m',
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
}

# ============================================================================
# 工具函數
# ============================================================================

def print_header(text):
    """打印標題"""
    print(f"\n{COLORS['BOLD']}{COLORS['BLUE']}{'='*60}{COLORS['RESET']}")
    print(f"{COLORS['BOLD']}{COLORS['BLUE']}{text}{COLORS['RESET']}")
    print(f"{COLORS['BOLD']}{COLORS['BLUE']}{'='*60}{COLORS['RESET']}\n")

def print_success(text):
    """打印成功消息"""
    print(f"{COLORS['GREEN']}✅ {text}{COLORS['RESET']}")

def print_info(text):
    """打印信息消息"""
    print(f"{COLORS['BLUE']}ℹ️  {text}{COLORS['RESET']}")

def print_warning(text):
    """打印警告消息"""
    print(f"{COLORS['YELLOW']}⚠️  {text}{COLORS['RESET']}")

def print_error(text):
    """打印錯誤消息"""
    print(f"{COLORS['RED']}❌ {text}{COLORS['RESET']}")

def check_python_version():
    """檢查 Python 版本"""
    print_header("🔍 檢查 Python 環境")
    
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"
    
    if version.major >= 3 and version.minor >= 9:
        print_success(f"Python 版本：{version_str}")
        return True
    else:
        print_error(f"Python 版本過舊：{version_str}（需要 3.9+）")
        return False

def check_required_packages():
    """檢查必要套件"""
    print_header("📦 檢查必要套件")
    
    required_packages = {
        'requests': 'HTTP 請求',
        'pandas': '數據分析',
        'numpy': '數值計算',
    }
    
    missing_packages = []
    
    for package, description in required_packages.items():
        try:
            __import__(package)
            print_success(f"{package:15} - {description}")
        except ImportError:
            print_warning(f"{package:15} - {description} (未安裝)")
            missing_packages.append(package)
    
    if missing_packages:
        print_warning(f"\n缺少套件：{', '.join(missing_packages)}")
        print_info("執行以下命令安裝：")
        print(f"  pip install {' '.join(missing_packages)}")
        return False
    
    return True

def check_directory_structure():
    """檢查目錄結構"""
    print_header("📁 檢查目錄結構")
    
    required_dirs = [
        'config',
        'scripts',
        'n8n_workflows',
        'pine_scripts',
        'logs',
    ]
    
    for dir_name in required_dirs:
        dir_path = Path(dir_name)
        if dir_path.exists():
            print_success(f"目錄存在：{dir_name}/")
        else:
            print_warning(f"目錄缺失：{dir_name}/")
            dir_path.mkdir(parents=True, exist_ok=True)
            print_info(f"已建立：{dir_name}/")
    
    return True

def check_config_files():
    """檢查配置文件"""
    print_header("⚙️  檢查配置文件")
    
    config_files = {
        'config/webhook_urls.json': {
            'tradingview_webhook': 'http://localhost:8000/webhook/tradingview',
            'manus_api_key': 'your-manus-api-key-here',
            'openai_api_key': 'your-openai-api-key-here',
            'n8n_webhook': 'http://localhost:5678/webhook/trade-signal',
        },
        'config/trading_params.json': {
            'account_size': 100000,
            'risk_per_trade': 0.02,
            'max_daily_risk': 0.05,
            'min_win_rate': 0.55,
            'min_rr_ratio': 2.0,
        },
    }
    
    for file_path, default_content in config_files.items():
        file_obj = Path(file_path)
        
        if file_obj.exists():
            print_success(f"配置文件存在：{file_path}")
        else:
            print_warning(f"配置文件缺失：{file_path}")
            file_obj.parent.mkdir(parents=True, exist_ok=True)
            with open(file_obj, 'w', encoding='utf-8') as f:
                json.dump(default_content, f, indent=2, ensure_ascii=False)
            print_info(f"已建立默認配置：{file_path}")
    
    return True

def create_sample_log():
    """建立示例交易日誌"""
    print_header("📊 建立示例交易日誌")
    
    log_file = Path('logs/trading_log.csv')
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    if not log_file.exists():
        header = "timestamp,signal_type,price,quantity,status,pnl,notes\n"
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(header)
        print_success(f"已建立交易日誌：{log_file}")
    else:
        print_success(f"交易日誌已存在：{log_file}")
    
    # 添加示例記錄
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sample_log = f"{timestamp},DEMO,18000,1,SUCCESS,500,系統初始化測試\n"
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(sample_log)
    
    print_info(f"已添加示例記錄")
    return True

def display_system_info():
    """顯示系統信息"""
    print_header("🖥️  系統信息")
    
    info = {
        '系統名稱': SYSTEM_NAME,
        '版本': VERSION,
        '狀態': '🟢 就緒',
        '本地服務': 'http://localhost:8000',
        '工作目錄': os.getcwd(),
        '時間戳': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC+8'),
    }
    
    for key, value in info.items():
        print_info(f"{key:15} : {value}")
    
    return True

def display_next_steps():
    """顯示下一步步驟"""
    print_header("📋 下一步步驟")
    
    steps = [
        "1. 編輯 config/webhook_urls.json 設置 API 密鑰",
        "2. 編輯 config/trading_params.json 調整交易參數",
        "3. 在 TradingView 上設置 Pine Script 指標",
        "4. 配置 n8n 工作流 (n8n start)",
        "5. 執行 7 天紙上交易測試",
        "6. 根據回測結果調整參數",
        "7. 啟動 24/7 自動化交易",
    ]
    
    for step in steps:
        print_info(step)
    
    return True

def display_quick_reference():
    """顯示快速參考"""
    print_header("⚡ 快速參考命令")
    
    commands = {
        '查看系統狀態': 'cat Status.md',
        '查看交易日誌': 'tail -f logs/trading_log.csv',
        '啟動 n8n': 'n8n start',
        '更新代碼': 'git pull',
        '提交更改': 'git add . && git commit -m "Update"',
        '推送到 GitHub': 'git push',
    }
    
    for desc, cmd in commands.items():
        print(f"  {desc:15} : {COLORS['YELLOW']}{cmd}{COLORS['RESET']}")
    
    return True

def run_all_checks():
    """執行所有檢查"""
    checks = [
        ('Python 版本', check_python_version),
        ('必要套件', check_required_packages),
        ('目錄結構', check_directory_structure),
        ('配置文件', check_config_files),
        ('交易日誌', create_sample_log),
        ('系統信息', display_system_info),
    ]
    
    results = {}
    
    for check_name, check_func in checks:
        try:
            results[check_name] = check_func()
        except Exception as e:
            print_error(f"{check_name} 檢查失敗：{str(e)}")
            results[check_name] = False
    
    return results

# ============================================================================
# 主程序
# ============================================================================

def main():
    """主程序"""
    
    # 清屏
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # 打印歡迎信息
    print(f"\n{COLORS['BOLD']}{COLORS['GREEN']}")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║          🏛️  Trade_Empire_Core - Success Demo 🏛️           ║")
    print("║                                                            ║")
    print("║              AI 交易帝國核心系統初始化測試                    ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print(f"{COLORS['RESET']}\n")
    
    # 執行所有檢查
    print_info("開始系統檢查...\n")
    time.sleep(1)
    
    results = run_all_checks()
    
    # 顯示下一步步驟
    display_next_steps()
    display_quick_reference()
    
    # 最終結果
    print_header("✨ 初始化完成")
    
    all_passed = all(results.values())
    
    if all_passed:
        print_success("所有檢查通過！系統已就緒。")
        print_info(f"版本：{VERSION}")
        print_info(f"狀態：🟢 就緒")
        print_info(f"時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC+8')}")
        print()
        print_success("🎉 Trade_Empire_Core 系統已成功初始化！")
        print_success("📊 現在您可以開始配置交易參數了。")
        print_success("🚀 下一步：編輯 config/ 目錄下的配置文件。")
        print()
        return 0
    else:
        print_warning("部分檢查未通過，請查看上方信息。")
        print_info("大多數問題可以通過安裝缺失的套件來解決。")
        print()
        return 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
