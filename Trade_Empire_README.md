# 🏛️ Trade_Empire_Core - AI 交易帝國核心系統

## 📌 系統願景

**主權在民** - 建立一個 24/7 自動化台指期交易系統，完全獨立於 Manus 配額限制，由用戶掌控全部資產和邏輯。

---

## 🎯 核心目標

| 目標 | 說明 |
|------|------|
| **24/7 自動運行** | 系統在本地或雲端持續運行，不依賴 Manus 會話 |
| **三層智能過濾** | 技術共鳴檢查 → 量價背離分析 → Manus 最終決策 |
| **配額節省** | 僅在高概率信號時調用 Manus，平時由本地 AI 代理執行 |
| **無縫會話銜接** | 通過 Status.md 追蹤系統狀態，Manus 視窗切換時無損繼續 |
| **自我進化** | 每週優化週期，持續改進交易邏輯 |

---

## 🏗️ 三層系統架構

### 第一層：信號源 (TradingView)
- **Pine Script 指標** 監控台指期 (TXFUSD)
- 檢測 Elliott Wave 波浪、Fibonacci 回調點、量價背離
- 實時推送信號到 n8n Webhook

### 第二層：本地執行引擎 (n8n / OpenClaw)
- **技術共鳴檢查**：驗證 Elliott Wave 波浪完整性
- **量價背離分析**：檢查成交量與價格的一致性
- **歷史模式匹配**：對比過去 52 週相似走勢
- 若信號通過二層過濾，推送至第三層

### 第三層：決策大腦 (Manus AI)
- 接收高概率信號
- 執行量子概率建模（可選高級分析）
- 生成最終交易建議與風險評估
- 發送 Webhook 回傳至 n8n 執行交易

---

## 🔧 技術棧

| 層級 | 技術 | 用途 |
|------|------|------|
| **信號生成** | TradingView Pine Script | 實時監控與指標計算 |
| **本地自動化** | n8n / Make | 工作流編排、API 整合 |
| **雲端託管** | Render / Railway | 24/7 無服務器運行 |
| **代碼倉庫** | GitHub (Trade_Empire_Core) | 版本控制與資產保存 |
| **決策引擎** | Manus AI / OpenAI API | 高級分析與決策 |
| **通訊協議** | Webhook / REST API | 系統間通訊 |

---

## 📊 交易分析方法

### 1. Elliott Wave Theory (波浪理論)
- 識別 5 浪上升與 3 浪下降模式
- 計算每個波浪的回調比例
- 預測第 5 浪目標位

### 2. Fibonacci Retracement (斐波那契回調)
- 0.382, 0.5, 0.618 回調位
- 識別支撐與阻力位
- 計算進場與止損點位

### 3. Volume-Price Divergence (量價背離)
- 成交量與價格方向一致性檢查
- 識別虛假突破
- 確認趨勢強度

### 4. Historical Pattern Recognition (歷史模式識別)
- 對比過去 52 週相似 K 線組合
- 計算相似度評分
- 基於歷史勝率預測

### 5. Quantum Probability Modeling (量子概率建模)
- 蒙特卡洛模擬未來 100 個走勢情景
- 計算各價格區間的概率分佈
- 生成風險調整後的期望收益

---

## 💰 配額節省策略

### Manus 調用時機
| 場景 | 調用頻率 | 成本估算 |
|------|---------|---------|
| 每日市場總結 | 1 次/天 | ~5 tokens/day |
| 高概率信號決策 | 2-3 次/天 | ~50 tokens/day |
| 週末系統優化 | 1 次/週 | ~100 tokens/week |
| **月度成本** | **~500 tokens** | **極低** |

### 本地執行成本
- n8n 自託管：免費
- Render 免費層：$0/月
- GitHub：免費（私有倉庫）
- **月度成本：$0**

---

## 🚀 快速開始

### 前置條件
- Windows PC 或 Mac
- GitHub 帳號（已完成 ✅）
- n8n 帳號（免費）
- TradingView 帳號（免費）

### 安裝步驟
詳見 `setup_guide.md`

### 首次測試
1. 執行 `Success_Demo.py` 驗證本地環境
2. 配置 TradingView Webhook
3. 啟動 n8n 工作流
4. 監控 Status.md 追蹤系統狀態

---

## 📈 預期收益

| 指標 | 目標 |
|------|------|
| **勝率** | 55-65% |
| **風險報酬比** | 1:2 以上 |
| **月度回報** | 5-15% |
| **最大回撤** | -10% 以內 |
| **系統可用性** | 99.5% |

---

## 🛡️ 風險管理

### 交易風險
- **單筆風險限制**：帳戶的 2%
- **每日風險限制**：帳戶的 5%
- **停損設置**：自動執行
- **頭寸管理**：動態調整

### 系統風險
- **備份機制**：GitHub 自動備份所有代碼
- **故障轉移**：多個 Webhook 端點
- **監控告警**：異常自動通知
- **日誌記錄**：所有交易完整追蹤

---

## 📋 文件結構

```
Trade_Empire_Core/
├── README.md                 # 本文件
├── setup_guide.md           # 安裝指南
├── Status.md                # 系統狀態追蹤
├── Success_Demo.py          # 首個本地測試腳本
├── config/
│   ├── trading_params.json  # 交易參數配置
│   └── webhook_urls.json    # Webhook 端點配置
├── scripts/
│   ├── elliott_wave.py      # 波浪理論計算
│   ├── fibonacci.py         # 斐波那契回調
│   ├── volume_analysis.py   # 量價分析
│   └── pattern_match.py     # 歷史模式識別
├── n8n_workflows/
│   ├── signal_filter.json   # 二層過濾工作流
│   └── trade_execution.json # 交易執行工作流
├── pine_scripts/
│   └── signal_generator.pine # TradingView 指標
└── logs/
    └── trading_log.csv      # 交易日誌
```

---

## 🔄 系統工作流

```
TradingView 信號
    ↓
n8n Webhook 接收
    ↓
[第一層] 技術共鳴檢查
    ↓ (通過)
[第二層] 量價背離分析
    ↓ (通過)
[第三層] Manus 最終決策
    ↓
交易執行 (買/賣/持有)
    ↓
結果記錄到 GitHub
    ↓
Status.md 更新
```

---

## 📞 支持與反饋

- **GitHub Issues**：報告 bug 或提出建議
- **Status.md**：查看系統狀態
- **logs/trading_log.csv**：查看交易歷史

---

## 📅 更新日誌

| 日期 | 版本 | 更新內容 |
|------|------|---------|
| 2026-02-01 | v0.1 | 初始架構設計 |
| TBD | v0.2 | TradingView 集成 |
| TBD | v1.0 | 完整系統上線 |

---

## ⚠️ 免責聲明

本系統僅供教育和研究用途。過去的表現不代表未來結果。使用本系統進行交易時，請自行承擔所有風險。建議在真實交易前進行充分的回測和紙上交易測試。

---

**最後更新**：2026-02-01  
**系統狀態**：🟢 開發中  
**下一步**：完成 setup_guide.md 與 Success_Demo.py
