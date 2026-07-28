clc;
clear;

// Read Excel File
a = readxls("C:\Users\Student\Desktop\Ankit_050_DM\Pract_3.xls");

// Read Sheet1
data = a(1);
data = sheet(3:17,3:4);

r = size(data, 1);

disp("users with self connections");

for i = 1:r
    if data(i,1) == data(i,2) then
        disp(data(i,1));
    end
end
