#include <stdio.h>

int main(void)
{
    int t, T, A, B, x, length;
    scanf("%d", &T);
    for (t = 1; t <= T; t++)
    {
        scanf("%d %d", &A, &B);
        x = B - A;
        length = x * (x+1) / 2;
        printf("#%d %d\n", t, length - B);
    }
    

    return 0;
}