#include <plot.h>
plsdev("x11"); // Use X11 graphics display
plinit();
int n = 10; // Number of data points
PLFLT x[n], y[n];

// Define data points
for (int i = 0; i < n; i++) {
    x[i] = i;
    y[i] = i * i;
}

pladv(0);
plvpor(0.1, 0.9, 0.1, 0.9); // Set the viewport
plwind(0.0, n - 1, 0.0, n * n); // Set the world window
plbox("bcnst", 0.0, 0, "bcnstv", 0.0, 0);

plpoin(n, x, y, 9); // Plot the data points

plend(); // Finish the plot

