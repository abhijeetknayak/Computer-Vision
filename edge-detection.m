pkg load image;

img = imread('peppers.jpg');
figure, imshow(img);

img_gray = rgb2gray(img);
figure, imshow(img_gray);

imgL = img_gray;
imgR = img_gray;

imgL(:, 1:size(imgL, 2) - 1) = imgL(:, 2:size(imgL)); % 'end' can be used too %
figure, imshow(imgL);

imgR(:, 2:size(imgR, 2)) = imgR(:, 1:size(imgR, 2) - 1);
figure, imshow(imgR);

edge_image = double(imgR) - double(imgL);
figure, imshow(edge_image, []);



