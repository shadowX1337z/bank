import random
#tạo lớp con nguoi
class con_nguoi:
  def __init__(self,ten,tuoi,gioi_tinh,nghe_nghiep):
    self.ten = ten
    self.tuoi = tuoi
    self.gioi_tinh = gioi_tinh
    self.nghe_nghiep = nghe_nghiep
  #tạo hàm nghề nghiệp để khai báo nghề nghiệp
  def get_nghe_nghiep(self):
    if self.tuoi <= 18:
      return "học sinh"
    elif 18 < self.tuoi < 25:
      return "sinh viên"
    else:
      if self.nghe_nghiep != "":
        return self.nghe_nghiep
      else:
        return "người đi làm"
  def hoat_dong(self):
    if self.tuoi < 25:
        return "học bài"
    else:
      return "làm việc"
#tạo lớp con bank_account
class bank_account(con_nguoi):
  def __init__(self,ten,tuoi,gioi_tinh,nghe_nghiep,so_tai_khoan,so_du,mat_khau_bank):
    super().__init__(ten,tuoi,gioi_tinh,nghe_nghiep)
    self.__so_tai_khoan = so_tai_khoan
    self.__so_du = so_du
    self.__mat_khau_bank = mat_khau_bank
    print("tạo tài khoản thành công")
    print("  ---chào mừng")
  def id_account(self):
    return self.__so_tai_khoan
  #xem số tiền còn lại trong tài khoản ngân hàng
  def check_balance(self):
    kiem_tra_mat_khau_bank = input("nhập mật khẩu tài khoản ngân hàng của bạn: ")
    if kiem_tra_mat_khau_bank == self.__mat_khau_bank:
      return self.__so_du
    else:
      return "mật khẩu sai"
#đầu vào người dùng
ten_nguoi = input("nhập tên: ")  #nhập tên người dùng
tuoi_nguoi = int(input("nhập tuổi: ")) #nhập tuổi người dùng
gioi_tinh_nguoi = input("nhập giới tính: ") #nhập giới tính người dùng
nghe_nghiep_nguoi = input("nhập nghề nghiệp: ") #nhập nghề nghiệp người dùng, nếu nghề nghiệp bỏ trống thì xác định nghề theo độ tuổi
#tao thông tin nguoi dùng
my_account = con_nguoi(ten_nguoi,tuoi_nguoi,gioi_tinh_nguoi,nghe_nghiep_nguoi)
#tao tai khoan ngan hang
while True:
  mat_khau_account_bank = input("tạo mật khẩu tài khoản ngân hàng: ")
  if len(mat_khau_account_bank) < 10:
    print("mật khẩu quá ngắn")
  elif len(mat_khau_account_bank) >= 35:
    print("mật khẩu quá dài")
  elif mat_khau_account_bank.isdigit():
    print("mật khẩu phải có thêm chữ cái")
  elif mat_khau_account_bank.isalpha():
    print("mật khẩu phải chứa thêm số")
  else:
    break
id_bank = random.randint(1000000000,9999999999)
so_du_tai_khoan = random.randint(200000,10000000)
bank = bank_account(ten_nguoi,tuoi_nguoi,gioi_tinh_nguoi,nghe_nghiep_nguoi,id_bank,so_du_tai_khoan,mat_khau_account_bank)
xem_stk = bank.id_account()
print("số tài khoản của bạn là: ",xem_stk)
xem_so_du = bank.check_balance()
print("số dư tài khoản của bạn là: ",xem_so_du)
