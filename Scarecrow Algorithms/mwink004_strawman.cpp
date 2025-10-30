// #include
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <random>
#include <cfloat>

using namespace std;

struct Point {
    double x, y;
};

double euclidianDist(const Point &a, const Point &b) {
    double x = a.x - b.x;
    double y = a.y - b.y;
    return sqrt(x*x + y*y);
}

int main() {
    cout << "ComputeDronePath (mwink004_strawman)" << endl;; 

    string fname;
    cout << "Enter the name of the file: ";
    cin >> fname;
    
    ifstream fin(fname);
    if (!fin) {
        cout << "Error: can't open file" << endl;
        return 1;
    }

    vector<Point> pts;
    double a;
    double b;
    while (fin >> a >> b) {
        pts.push_back({a, b});
    }

    int N = pts.size();
    // error handle?

    cout << "There are " << N << " nodes, computing route.." << endl;
    cout << "\t Shortest Route Discovered So Far" << endl;

    // matrix
    vector<vector<double>> Distance(N, vector<double>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            Distance[i][j] = euclidianDist(pts[i], pts[j]);
        }
    }

    vector<int> currBest;
    double bestSoFar = DBL_MAX;

    // create order of visitation
    vector<int> permutation; 
    for (int i = 0; i < N; i++) {
        permutation.push_back(i);
    }

    // randomize order of visitation
    auto rng = default_random_engine{}; 
    // better rng since my thing was convering the exact same
    random_device rd;
    rng.seed(rd());

    // anytime algorithm
    while (true)
    {
        shuffle(begin(permutation) + 1, end(permutation), rng); // random permutation but keep one at index 0 the same

        double total = 0.0;
        int curr = 0;
        for (int i = 1; i < N; i++)
        { 
            total += Distance[curr][permutation[i]];
            curr = permutation[i];
        }
        total += Distance[curr][0]; // start node

        if (total < bestSoFar) {
            bestSoFar = total;
            currBest = permutation;
            cout << "\t\t" << bestSoFar << endl;
        }
    }

    //cout << "Best route found:" << endl;

    //for (int i = 0; i < N; i++) {
        //cout << (bestTour[i] + 1) << " ";
    //}
    //cout << 1 << endl; // return to start

    return 0;
}