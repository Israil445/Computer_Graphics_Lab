#include <graphics.h>
#include <bits/stdc++.h>

using namespace std;

void drawTriangle() {
    vector<int> x = {10, 50, 100};
    vector<int> y = {100, 20, 100};

    setcolor(GREEN);
    line(x[0], y[0], x[1], y[1]);
    line(x[1], y[1], x[2], y[2]);
    line(x[2], y[2], x[0], y[0]);

    setfillstyle(SOLID_FILL, GREEN);
    floodfill((x[0]+x[1]+x[2])/3, (y[0]+y[1]+y[2])/3, GREEN); 
}


void drawCircle()
{
    setcolor(BLUE);
    circle(100, 100, 45);
    setfillstyle(SOLID_FILL, BLUE);
    floodfill(101, 101, BLUE);
}

void drawRectangle()
{
    setcolor(RED);
    rectangle(100, 100, 180, 180);
    setfillstyle(SOLID_FILL, RED);
    floodfill(101, 101, RED);
}

int main()
{
    int gd = DETECT, gm = DETECT;
    initgraph(&gd, &gm, "");

    string sequence = "RCT";
    for (char x: sequence)
    {
        if (x == 'C') drawCircle();
        else if (x == 'T') drawTriangle();
        else drawRectangle();
    }

    getch();
    closegraph();
    return 0;
}