import PIL
from PIL import Image
with open(r"C:\Users\softl\Documents\python\.ipynb_checkpoints\hello_there\image_secret_2.txt", "r") as file:
    file = file.read()
    file_length = len(file)
    def factoring():
        for i in range(1000, int(file_length**0.5 + 1)):
            step_one = [file_length // i, i]
            M = step_one[0]
            N = step_one[1]
            if M*N == file_length:
                yield M
                yield N

    def matrix(x,y):
            m = 1460
            n = 1096
        # for m in factoring(): 
            # n = int(file_length / m)
            # print(m,n)
            image = Image.new("RGBA", (m,n), "black")   
            x = 0
            y = 0
            for pix in file:

                if pix == "1":
                

                    if x == m:
                        y += 1
                        x = 0

            
                    image.putpixel((x,y),(255,0,0))
                else:
                        if x == m:
                            y += 1
                            x = 0
                x += 1
        
            image.save("шарики_за_ролики.png", "PNG")
            input()


    matrix(0,0)
    #half_length = int(range(2, file_length//2)
    #factoring = file_length // half_length
    #print(factoring)

    #xPoint = n % M
    #yPoint = n // N
    #for i in file:
