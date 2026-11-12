# Japan Winter Trip 2026 · GitHub Pages

六日五夜日本行程網站（繁體中文／廣東話），涵蓋 2026 年 12 月 22–27 日交通、景點、住宿、餐飲、預算及預訂待辦。

## 直接部署 GitHub Pages

1. 在 GitHub 建立一個新的 public 或 private repository（是否支援 Pages 視乎帳戶與設定）。
2. 上傳本資料夾中的 `index.html` 到 repository 根目錄。
3. 到 **Settings → Pages**，在 **Build and deployment** 選擇 **Deploy from a branch**。
4. Branch 選 `main`，folder 選 `/(root)`，儲存並等候部署。
5. 以 GitHub 顯示的 Pages 網址開啟網頁。

## 使用

- 頂部分頁：總覽、Day 1–6、住宿＋Meals、預算、待辦＋連結。
- 預算頁：可調整 JPY→HKD 匯率；將同步更新港幣換算。
- 待辦頁：可以勾選已完成項目。
- 匯率及勾選狀態存在瀏覽器 `localStorage`，**不會同步不同手機，也不會更新 Google Sheets**。
- 不需要 Node.js、npm、資料庫或第三方 CSS／JS 套件，`index.html` 可直接在瀏覽器開啟。

## 資料維護

更改 `index.html` 中 `<script>` 裡的 `DATA` 常數：
- `rate`：預設日圓兌港幣匯率
- `days`：每天時間軸
- `hotels`：住宿與套餐
- `budget`：金額表
- `tasks`：待辦
- `sources`：官方網站連結

**資料狀態**：2026-11-12 規劃版本。航班已購；其他預訂須以正式確認信為準。冬季上高地雪況和公共交通可能調整。請勿公開任何訂單編號、護照資料或個人聯絡方式。
