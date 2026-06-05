## Mục tiêu

Hoàn thiện quá trình **Phỏng vấn Khám phá & Xác định Bài toán**, kiểm tra **AI Readiness**, lựa chọn mức độ giải pháp phù hợp, đánh giá tính khả thi và chốt quyết định **Go / Not Yet / No-Go**.

---

## 1. Phỏng vấn Khám phá & Xác định Bài toán - Problem Scoping

### 1.1. Chuẩn bị phỏng vấn stakeholder

- [ ] Viết kịch bản phỏng vấn user thật.
- [ ] Xác định các bên liên quan - Stakeholder cần phỏng vấn.
- [ ] Xác định **Actor / Operator**: Ai đang làm công việc này hằng ngày?
- [ ] Chuẩn bị câu hỏi để làm rõ hiện trạng trước khi nghĩ đến giải pháp.

### 1.2. Khảo sát current workflow

- [ ] Vẽ lại **Current Workflow**: Hiện tại họ đang xử lý qua những bước nào?
- [ ] Ghi nhận các công cụ - tool - đang được sử dụng trong từng bước.
- [ ] Xác định bước nào đang cần tổng hợp quá nhiều thông tin.
- [ ] Xác định bước nào đang chậm.
- [ ] Xác định bước nào dễ lỗi.
- [ ] Xác định bước nào không nhất quán.

### 1.3. Tìm pain thật và bottleneck

- [ ] Từ phỏng vấn rút ra **pain thật**.
- [ ] So sánh **pain thật** với **giả định pain của đề tài**.
- [ ] Tìm ra **Bottleneck - Điểm nghẽn** trong workflow hiện tại.
- [ ] Ghi rõ bottleneck nằm ở bước nào của workflow.
- [ ] Ghi rõ bottleneck liên quan đến chậm, dễ lỗi, không nhất quán, hay cần tổng hợp quá nhiều thông tin.

### 1.4. Đo lường impact

- [ ] Đo lường tổn thất về thời gian.
- [ ] Đo lường tổn thất về chi phí.
- [ ] Đo lường ảnh hưởng đến SLA.
- [ ] Đo lường error rate nếu có.
- [ ] Đo lường ảnh hưởng đến tỷ lệ chuyển đổi nếu có.

### 1.5. Thiết lập success metric

- [ ] Xác định khi nào hệ thống được coi là thành công.
- [ ] Xác định mức ngưỡng đạt được cho từng success metric.
- [ ] Ghi rõ metric nào dùng để so sánh trước và sau khi triển khai.

### 1.6. Xác định operational boundary

- [ ] Xác định nếu AI làm sai thì sao.
- [ ] Xác định hệ thống được phép làm gì.
- [ ] Xác định hệ thống không được phép làm gì.
- [ ] Xác định điểm nào cần con người can thiệp - Human-in-the-loop, HITL.

---

## 2. Kiểm tra AI Readiness

Trả lời 5 câu hỏi sau để quyết định dự án có đáng để dùng AI không.

### 2.1. Value

- [ ] Bài toán này có xảy ra thường xuyên không?
- [ ] Bài toán này có thực sự đang làm tốn thời gian không?
- [ ] Bài toán này có thực sự đang làm tốn tiền bạc không?
- [ ] Bài toán này có thực sự ảnh hưởng đến SLA không?

### 2.2. Baseline

- [ ] Hiện tại đã có quy trình thủ công - manual - để làm mốc so sánh chưa?
- [ ] Hiện tại đã có workflow baseline để làm mốc so sánh chưa?

### 2.3. Eval

- [ ] Đã có bộ chỉ số - metric - để đánh giá kết quả chưa?
- [ ] Đã có các case mẫu để đánh giá kết quả chưa?
- [ ] Đã có log dữ liệu để đánh giá kết quả chưa?
- [ ] Việc đánh giá có thể lặp lại - reproducible - không?

### 2.4. Tolerance

- [ ] Mức độ sai số hữu hạn có thể chấp nhận được không?
- [ ] Đã có chốt chặn con người - HITL - ở các điểm quan trọng chưa?

### 2.5. Operations

- [ ] Đã có người chịu trách nhiệm - owner - chưa?
- [ ] Đã có cơ chế rollback - hoàn tác - chưa?
- [ ] Đã có logging chưa?
- [ ] Đã có chính sách xử lý khi output bị sai chưa?

### 2.6. Quyết định AI Readiness

- [ ] Đếm số câu trả lời **YES** trong 5 nhóm trên.
- [ ] Nếu dưới 3 câu trả lời **YES**, dừng lại và làm rõ bài toán hoặc quy trình trước khi đầu tư vào AI.

---

## 3. Lựa chọn Mức độ Giải pháp - Architecture Choice

Nguyên tắc: đi từ đơn giản đến phức tạp, chỉ nâng cấp khi giá trị tạo ra lớn hơn độ phức tạp.

### 3.1. Rule / Script

- [ ] Kiểm tra input có ổn định không.
- [ ] Kiểm tra logic có rõ ràng không.
- [ ] Kiểm tra yêu cầu predictability có cao không.
- [ ] Kiểm tra yêu cầu compliance có khắt khe không.
- [ ] Nếu các điều kiện trên phù hợp, ưu tiên **Rule / Script**.

### 3.2. LLM Feature

- [ ] Kiểm tra input có biến thể vừa phải không.
- [ ] Kiểm tra output có cần tính linh hoạt không.
- [ ] Kiểm tra đã có metric chưa.
- [ ] Kiểm tra đã có guardrails chưa.
- [ ] Kiểm tra con người có thể review lại không.
- [ ] Nếu các điều kiện trên phù hợp, cân nhắc **LLM Feature**.

### 3.3. Agent

- [ ] Kiểm tra bài toán có cần xử lý qua nhiều bước không.
- [ ] Kiểm tra bài toán có cần gọi nhiều tool không.
- [ ] Kiểm tra trạng thái có thay đổi liên tục không.
- [ ] Kiểm tra có cần ra quyết định động không.
- [ ] Kiểm tra đã có kiểm soát rủi ro rõ ràng chưa.
- [ ] Chỉ sử dụng **Agent** nếu các điều kiện trên thật sự cần thiết.

---

## 4. Đánh giá Tính khả thi Cuối cùng - Feasibility Check

### 4.1. Feasibility Kỹ thuật

- [ ] Đã có baseline để so sánh chưa?
- [ ] Có đủ data/docs để đánh giá - eval - không?
- [ ] Latency có chấp nhận được không?
- [ ] Cost/task có chấp nhận được không?
- [ ] Kiến trúc có thể làm đơn giản hơn không?

### 4.2. Feasibility Vận hành

- [ ] Đã có hệ thống logging chưa?
- [ ] Đã có monitoring chưa?
- [ ] Có HITL khi cần không?
- [ ] Có quy trình phê duyệt - approvals - khi cần không?
- [ ] Có rollback path khi output sai không?
- [ ] Có owner rõ ràng khi output sai không?

### 4.3. Feasibility Kinh doanh

- [ ] ROI có dương ở phạm vi pilot không?
- [ ] Các vấn đề về rủi ro đã rõ ràng chưa?
- [ ] Các vấn đề về tuân thủ đã rõ ràng chưa?
- [ ] Ops team có sẵn sàng thay đổi quy trình làm việc không?
- [ ] Giá trị mang lại có đủ lớn để bù đắp cho độ phức tạp của hệ thống không?

### 4.4. Kết luận Feasibility

- [ ] Nếu không trả lời được 2-3 câu hỏi ở mỗi khía cạnh, chưa xây dựng Agent.
- [ ] Nếu chưa sẵn sàng làm Agent, chuyển hướng sang workflow nhỏ hơn.
- [ ] Nếu chưa đủ dữ liệu, tiếp tục thu thập thêm dữ liệu.

---

## 5. Câu hỏi cần chuẩn bị

### 5.1. Câu hỏi để hỏi mentor

- [ ] Baseline hiện tại đã đủ để so sánh chưa?
- [ ] Metric nào nên dùng để đánh giá kết quả?
- [ ] Case mẫu hoặc log dữ liệu hiện tại đã đủ để eval chưa?
- [ ] Mức sai số nào có thể chấp nhận được?
- [ ] Điểm nào bắt buộc cần HITL?
- [ ] Nên chọn Rule / Script, LLM Feature, hay Agent?
- [ ] Kiến trúc hiện tại có thể làm đơn giản hơn không?
- [ ] Risk controls hiện tại đã đủ rõ ràng chưa?
- [ ] Điều kiện nào để chốt Go / Not Yet / No-Go?

### 5.2. Câu hỏi để hỏi host amazone

- [ ] Ai đang làm công việc này hằng ngày?
- [ ] Hiện tại công việc được xử lý qua những bước nào?
- [ ] Hiện tại đang sử dụng những tool gì?
- [ ] Bước nào đang bị chậm?
- [ ] Bước nào dễ lỗi?
- [ ] Bước nào không nhất quán?
- [ ] Bước nào cần tổng hợp quá nhiều thông tin?
- [ ] Vấn đề này đang gây tổn thất bao nhiêu về thời gian?
- [ ] Vấn đề này đang gây tổn thất bao nhiêu về chi phí?
- [ ] Vấn đề này có ảnh hưởng đến SLA không?
- [ ] Vấn đề này có ảnh hưởng đến error rate không?
- [ ] Vấn đề này có ảnh hưởng đến tỷ lệ chuyển đổi không?
- [ ] Khi nào hệ thống được coi là thành công?
- [ ] Nếu AI làm sai thì quy trình xử lý là gì?
- [ ] Hệ thống được phép làm gì?
- [ ] Hệ thống không được phép làm gì?
- [ ] Điểm nào cần con người can thiệp?

---

## 6. Chốt Quyết định - Go / Not Yet / No-Go

### 6.1. Go

- [ ] Chọn **Go** nếu bài toán rõ ràng.
- [ ] Chọn **Go** nếu đã có baseline.
- [ ] Chọn **Go** nếu có phương án đánh giá - eval.
- [ ] Chọn **Go** nếu có kiểm soát rủi ro - risk controls - rõ ràng.

### 6.2. Not Yet

- [ ] Chọn **Not Yet** nếu pain là có thật nhưng đang thiếu dữ liệu.
- [ ] Chọn **Not Yet** nếu đang thiếu metric.
- [ ] Chọn **Not Yet** nếu ranh giới của workflow chưa rõ ràng.

### 6.3. No-Go

- [ ] Chọn **No-Go** nếu rule-based đã xử lý đủ tốt.
- [ ] Chọn **No-Go** nếu hậu quả khi AI sai là quá đắt đỏ.
- [ ] Chọn **No-Go** nếu chi phí thay đổi lớn hơn giá trị mang lại.

---

## 7. Definition of Done

- [ ] Đã hoàn thành kịch bản phỏng vấn user thật.
- [ ] Đã phỏng vấn stakeholder cần thiết.
- [ ] Đã vẽ Current Workflow.
- [ ] Đã xác định Actor / Operator.
- [ ] Đã xác định Bottleneck.
- [ ] Đã rút ra pain thật từ phỏng vấn.
- [ ] Đã so sánh pain thật với giả định pain của đề tài.
- [ ] Đã đo lường Impact.
- [ ] Đã thiết lập Success Metric.
- [ ] Đã xác định Operational Boundary.
- [ ] Đã kiểm tra AI Readiness.
- [ ] Đã lựa chọn mức độ giải pháp phù hợp.
- [ ] Đã đánh giá Feasibility kỹ thuật.
- [ ] Đã đánh giá Feasibility vận hành.
- [ ] Đã đánh giá Feasibility kinh doanh.
- [ ] Đã chuẩn bị câu hỏi cho mentor.
- [ ] Đã chuẩn bị câu hỏi cho host amazone.
- [ ] Đã chốt quyết định Go / Not Yet / No-Go.
