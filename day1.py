# Level 1: Fundamental
"""
	NumPy(Numerical Python) là thư viện nền móng  của toàn bộ hệ sinh thái data/ML bằng python.
- Cốt lõi của NumPy là ndarray (N-dimensional array) và dù code bằng python thì NumPy dùng C để xử lý các tính toán.
- Pandas được xây dựng dựa trên NumPy thì Pandas mang đến một lớp giao diện (DataFrame) giống như bảng Excel, có tên hàng, tên cột, và xử lý được cả text, thời gian, số liệu hỗn hợp.
=> sử dụng: Pandas để làm sạch, lọc, và chuẩn bị dữ liệu (Data Analysis). Sau đó, chuyển dữ liệu đó thành NumPy array để đẩy vào các mô hình Machine Learning/Deep Learning tính toán.

* Các thư viện Scikit-learn, TensorFlow, Pytorch sẽ dùng NumPy như một định dạng chuẩn để giao tiếp và NumPy giúp chuẩn hóa cách lưu trữ số liệu và cung cấp các phép toán tuyến tính (Linear Algebra) được tối ưu hóa tận mức phần cứng (CPU/GPU).

* Khái niệm quan trọng 'Memory Layout': chỉ chứa một kiểu dữ liệu duy nhất. Dữ liệu được sắp xếp cạnh nhau thành một khối duy nhất trong RAM, chính vì điều đó CPU có thể bốc một mạch toàn bộ dữ liệu vào bộ nhớ đệm (cache-friendly).

* Hơn nữa nó còn áp dụng 'Vectorization'(nhờ công nghệ SIMD của CPU) - thay vì cộng từng số một như vòng lặp for thì nó sẽ ra lệnh cho CPU cộng cùng một lúc 8 hoặc 16 cặp số trong cùng một xung nhịp.
"""

# Bài học số 1: ndarray & RAM
''' khởi tạo mảng NumPy '''
import numpy as np

# tạo một ma trận 2D (3 hàng - 3 cột)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Ma trận:\n", matrix)
print("Hình dáng (shape): ", matrix.shape)
print("Tổng số phần tử (size): ", matrix.size)

# kiểm tra memory layout bên dưới dùng .flags[]
print("C-contiguous (row-major): ", matrix.flags['C_CONTIGUOUS']) # kiểm tra hàng ngang liên tục
print("F-contiguous (column-major): ", matrix.flags['F_CONTIGUOUS']) # kiểm tra hàng dọc liên tục

# trực quan hoá cách máy tính nhìn mảng trên
"""
Địa chỉ RAM:  [x+0] [x+4] [x+8]  [x+12] [x+16] [x+20]  [x+24] [x+28] [x+32]
Dữ liệu:      [ 1 ] [ 2 ] [ 3 ]  [ 4  ] [ 5  ] [ 6  ]  [ 7  ] [ 8  ] [ 9  ]
              |___Hàng 1______|  |____Hàng 2________|  |____Hàng 3________|

lưu ý: Mỗi số nguyên int32 chiếm 4 bytes, nên địa chỉ RAM cách nhau 4 đơn vị.
"""

# khi biết trước kích thước của ma trận, hãy tạo mảng trống bằng 'np.zeros() hoặc np.ones()' sau đó điền dữ liệu vào.
khung_du_lieu = np.zeros((1000, 1000)) # ma trận 1000x1000
print('----------------------------------------------------------')

# Bài học số 2: DTYPE, shape & cạm bẫy bộ nhớ
''' 1. Cạm bẫy tràn số (Overflow) với dtype '''
# xảy ra khi ép NumPy dùng vùng nhớ nhỏ như 'uint8' để chứa kết quả của một phép toán vượt quá giới hạn, nó sẽ không báo lỗi mà âm thầm quay vòng giá trị (wrap around). Trong xử lí ảnh, lỗi này khiến ảnh bị sai màu hoặc xuất hiện các đốm nhiễu kì lạ.

pixels = np.array([250, 100, 50], dtype=np.uint8) # mảng điểm ảnh kiểu uint8 (chỉ chứa số từ 0 -> 255)
pixels_new = pixels + 10 # cộng thêm 10 vào tất cả (250 + 10 = 260 vượt qua 255)
print("Sau khi cộng 10: ", pixels_new) #output: [4 110 60] -> chạm ngưỡng 255, sau đó đếm ngược từ 0

# => khi thực hiện các phép toán phức tạp (tăng sáng, blend ảnh), Engineer luôn chuyển (cast) dữ liệu sang kiểu float32 hoặc int32 để tính toán trước, sau đó giới hạn lại trong khoảng 0-255 và ép kiểu ngược về uint8.

''' 2. Shape và ReShape '''
arr_1d = np.array([1,2,3,4,5,6]) # mảng 1 chiều 6 phần tử
maxtrix_2d = arr_1d.reshape(2, 3) # cấu trúc lại thành mảng 2 hàng x 3 cột
print("Ma trận 2x3:\n", maxtrix_2d)
# Bản chất bên trong hàm .reshape() chạy gần như tức thời O(1) vì numpy không xáo trộn hay di chuyển dữ liệu trong RAM, chỉ đơn giản là thay đổi cách đọc ngắt quãng ở đâu (trong th trên là sau số 3 thì xuống dòng). Và .reshape() không tạo mảng mới trong RAM.
print('----------------------------------------------------------')

# Bài học số 3: View & Copy - bài toán về toàn vẹn dữ liệu
''' 1. Bản chất của View '''
# khi dùng hàm .reshape(), NumPy không hề cấp phát thêm RAM để tạo ra một ma trận mới. Thay vào đó, nó tạo ra một View (một góc nhìn mới, một lăng kính mới) chiếu thẳng vào dải bộ nhớ gốc.

arr = np.array([1, 2, 3, 4])
mtrix = arr.reshape(2, 2)
mtrix[0, 0] = 99
print(arr) #output: [99,2,3,4]

# Vì cả hai cùng trỏ chung vào một vùng RAM, khi bạn thay đổi dữ liệu qua matrix, dữ liệu gốc bên dưới bị thay đổi, dẫn đến arr cũng thấy sự thay đổi đó.
# trực quan hoá:
"""
Lăng kính 'arr' (1D):      [0]       [1]       [2]       [3]
                            |         |         |         |
RAM THỰC TẾ:             [  99  ]  [  2  ]  [  3  ]  [  4  ]
                            |         |         |         |
Lăng kính 'matrix' (2D): [0,0]     [0,1]     [1,0]     [1,1]
"""
'''2. Tại sao NumPy lại thiết kế như vậy ?'''
#-> hướng đến Performance, thiết kế của NumPy tối ưu hoá tối đa việc tái sử dụng bộ nhớ(ví dụ trong th xử lý 10tr ảnh-500GB, nếu mỗi lần reshape để đưa vào mô hình DL mà máy tính lại copy ra một bản mới thì sẽ sập vì hết RAM).

'''3. Cách khắc phục '''
# nếu muốn tạo ra ma trận mới mà không làm hỏng ma trận gốc thì sử dụng hàm .copy()

arr3 = np.array([1,2,3,4])
mtrix3 = arr3.reshape(2,2).copy() # dùng .copy() ép NumPy cấp phát một vùng RAM mới
mtrix3[0,0] = 99
print("Mảng gốc: ", arr3) #output: [1,2,3,4] - dữ liệu gốc được đảm bảo

# Indexing & Slicing (Truy xuất và Cắt mảng). Slicing trong NumPy có cú pháp là [start:stop:step]
"""
	array[a:b, c:d]
-> a:b → lấy các hàng từ vị trí a đến trước b
-> c:d → lấy các cột từ vị trí c đến trước d
"""
print('----------------------------------------------------------')


# Level 2: Core Operations
# Bài học số 4: Boolean Masking & Vectorization
''' 1. Tại sao cần đến ? '''
# Ở phần trên chúng ta dùng [1:3] để cắt mảng khi biết trước vị trí. Nhưng trong thực tế ML, hiếm khi biết trước được vị trí. ví dụ hệ thống yêu cầu: "Hãy tìm cho tôi tất cả các pixel bị chói sáng (giá trị > 240)", hoặc "Lọc ra các khách hàng có tuổi < 18"
# -> giải pháp của NumPy là: Gửi một "điều kiện" xuống C backend, CPU sẽ dùng công nghệ SIMD (Single Instruction, Multiple Data) để so sánh hàng loạt các con số cùng một lúc. Kết quả trả về là một mảng gồm các giá trị True/False (gọi là Mặt nạ - Mask).

''' 2. Ví dụ thực tế: Cảnh báo nhịp tim bất thường '''
# Giả sử chúng ta đang code hệ thống cho smartwatch, thiết bị thu về một mảng nhịp tim trong ngày và bạn cần lọc ra những nhịp tim nguy hiểm (> 100 nhịp/phút)
nhip_tim = np.array([72, 85, 110, 65, 130, 75])
mat_na = nhip_tim > 100 #Bước 1: VECTORIZATION (so sánh toàn bộ mảng cùng một lúc, CPU xử lý // không cần for)
print("Mặt nạ Boolean:", mat_na)
canh_bao = nhip_tim[mat_na] #Bước 2: MASKING (chỉ dữ lại những vị trí có giá trị TRUE)
print("Các nhịp tim nguy hiểm: ", canh_bao) #output: [110, 130]
# Performance: Toàn bộ quá trình này chạy ở tốc độ của ngôn ngữ C.
# Trực quan hoá của MASK
"""
Dữ liệu gốc:  [  72,    85,   110,    65,   130,    75  ]
Mặt nạ:       [False, False,  True, False,  True, False ]
              -------------------------------------------
Kết quả lọc:                  [110]         [130]
"""




