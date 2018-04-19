#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define NUM_ROWS 20
#define NUM_COLS 20

vector<vector<int> > matrix;
long int calculate_vertical(int row, int col);
long int calculate_horizontal(int row, int col);
long int calculate_back_diagonal(int row, int col);
long int calculate_front_diagonal(int row, int col);

int main() {
    string rawInput;
    for(int i = 0; i < 20; i++) {
        vector<int> row;
        for(int j = 0; j < 20; j++) {
            cin >> rawInput;
            row.push_back(stoi(rawInput));
        }
        matrix.push_back(row);
    }

    long int biggest_product = 0;
    long int _vertical = 0, 
         _horizontal = 0, 
         _back_diagonal = 0, 
         _front_diagonal = 0;

    for(int i = 0; i < NUM_ROWS; i++) {
        for(int j = 0; j < NUM_COLS; j++) {
            _vertical = calculate_vertical(i, j);
            _horizontal = calculate_horizontal(i, j);
            _back_diagonal = calculate_back_diagonal(i, j);
            _front_diagonal = calculate_front_diagonal(i, j);

            if(_vertical > biggest_product)
                biggest_product = _vertical;
            if(_horizontal > biggest_product)
                biggest_product = _horizontal;
            if(_back_diagonal > biggest_product)
                biggest_product = _back_diagonal;
            if(_front_diagonal > biggest_product)
                biggest_product = _front_diagonal;
        }
    }

    cout << biggest_product << endl;

    return 0;
}

long int calculate_vertical(int row, int col) {
    if(row > NUM_ROWS-4)
        return 0;

    return matrix[row][col] * 
        matrix[row+1][col] * 
        matrix[row+2][col] *
        matrix[row+3][col];
}

long int calculate_horizontal(int row, int col) {
    if(col > (NUM_COLS-3))
        return 0;

    return matrix[row][col] *
        matrix[row][col+1] *
        matrix[row][col+2] *
        matrix[row][col+3];
}

long int calculate_back_diagonal(int row, int col) {
    if(col < 3 || (row > NUM_ROWS-4))
        return 0;

    return matrix[row][col] *
        matrix[row+1][col-1] *
        matrix[row+2][col-2] *
        matrix[row+3][col-3];
}

long int calculate_front_diagonal(int row, int col) {
    if(col > (NUM_COLS-3) || (row > NUM_ROWS-4))
        return 0;

    return matrix[row][col] *
        matrix[row+1][col+1] *
        matrix[row+2][col+2] *
        matrix[row+3][col+3];
}
