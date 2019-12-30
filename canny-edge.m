% For Your Eyes Only
pkg load image;

frizzy = imread('frizzy.png');
froomer = imread('froomer.png');
imshow(frizzy);
imshow(froomer);

% TODO: Find edges in frizzy and froomer images
f1 = rgb2gray(frizzy);
f2 = rgb2gray(froomer);
edge_im = edge(f1, 'canny');
edge_im2 = edge(f2, 'canny');
imshow(edge_im);
imshow(edge_im2);

% TODO: Display common edge pixels

final = edge_im .* edge_im2;
imshow(final);