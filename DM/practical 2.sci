clc;
clear;
file=readxls("C:\Users\Student\Downloads\Cafe_menu.xls");
sheet1=file(1);
m=sheet1.text(10:13,3);
disp(m)
// Extract first three menu items
three = sheet1.text(10:12,3);

// Display Power Set
disp("Power Set");

disp("{}");                    // Empty Set

disp(m(1));                    // Single-item subsets
disp(m(2));
disp(m(3));

disp("{" + m(1) + ", " + m(2) + "}");       // Two-item subsets
disp("{" + m(1) + ", " + m(3) + "}");
disp("{" + m(2) + ", " + m(3) + "}");
disp("{" + m(1) + ", " + m(2) + ", " + m(3) + "}");       // Three-item subsets
// Number of selected menu items
n = 3;

// Calculate total subsets
subsets = 2^n;

// Display result
disp("Number of Menu Items:");
disp(n);

disp("Total Number of Subsets:");
disp(subsets);
//Number of menu items
disp("Number of Menu Items:");
n1=5;
total_subsets = 2^n1;
disp(total_subsets)
// Sum using loop
sum1 = 0;
for i = 1:n1
    sum1 = sum1 + i;
end

// Formula
sum2 = n1*(n1+1)/2;
  
// Display results

disp(n1);

disp("Sum using Loop:");
disp(sum1);

disp("Sum using Formula:");
disp(sum2);

// Verify
if sum1 == sum2 then
    disp("Mathematical Induction Formula Verified");
else
    disp("Formula Not Verified");
end
