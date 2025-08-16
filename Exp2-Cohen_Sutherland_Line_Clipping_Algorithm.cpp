#include <graphics.h>
#include <bits/stdc++.h>

using namespace std;

// Clipping Window Parameters
double x_left = 150, x_right = 450, y_bottom = 120, y_top = 320;

// Region Code Constants
int Left = 1, Right = 2, Bottom = 4, Top = 8;

// Function to calculate region code for a point
int regionCode(int x, int y) {
    int code = 0;
    if (x > x_right) code |= Right;
    else if (x < x_left) code |= Left;
    if (y > y_top) code |= Top;
    else if (y < y_bottom) code |= Bottom;
    return code;
}

// Cohen-Sutherland Line Clipping Algorithm
void cohenSutherland(double x1, double y1, double x2, double y2) {
    int code1 = regionCode(x1, y1);
    int code2 = regionCode(x2, y2);

    while (true) {
        double x, y;
        if (!(code1 | code2)) {  // Line completely inside
            line(x1, y1, x2, y2);
            return;
        } else if (code1 & code2) { // Line completely outside
            break;
        } else { // Line partially inside
            int code = code1 ? code1 : code2;

            if (code & Top) {
                y = y_top;
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1);
            } else if (code & Bottom) {
                y = y_bottom;
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1);
            } else if (code & Left) {
                x = x_left;
                y = y1 + (y2 - y1) * (x - x1) / (x2 - x1);
            } else if (code & Right) {
                x = x_right;
                y = y1 + (y2 - y1) * (x - x1) / (x2 - x1);
            }

            if (code == code1) {
                x1 = x; y1 = y;
                code1 = regionCode(x1, y1);
            } else {
                x2 = x; y2 = y;
                code2 = regionCode(x2, y2);
            }
        }
    }
}

int main() {
    int gd = DETECT, gm = DETECT;
    initgraph(&gd, &gm, "");

    // Draw clipping window 
    setcolor(YELLOW);
    rectangle(x_left, y_bottom, x_right, y_top);
    //rectangle(x_left, y_top, x_right, y_bottom);
    
    // Draw original line 
    double x1 = 120, y1 = 50, x2 = 350, y2 = 400;

    setcolor(YELLOW);
    line(x1, y1, x2, y2);

    // Draw clipped line in GREEN
    setcolor(WHITE);
    cohenSutherland(x1, y1, x2, y2);

    getch();
    closegraph();
    return 0;
}

