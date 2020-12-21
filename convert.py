import cv2
x=0
test=[6,23,40,44,57,61,64,74,82,91,99,104,108,112,120,125,131,133,142,150,155,159,176,
181,182,183,193,196,210,211,212,227,236,244,261,278,294,295,297,311,312,314,316,318,319,
320,329,335,336,346,349,363,378,380,384,395,397,414,421,427,431,438,448,461,465,482,485,499]
new_width = 481
new_height = 321
dim = (new_width, new_height)
for i in test:
	img = cv2.imread("test/"+str(test[x])+".jpg", cv2.IMREAD_UNCHANGED)
	dresized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	cv2.imwrite('trainx/'+str(test[x])+'.jpg', dresized)
	x=x+1
