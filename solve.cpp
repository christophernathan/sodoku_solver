#include <iostream>
using namespace std;

#define N 9

void printBoard(int board[N][N]){
    for (int a=0; a<N; a++){
        for (int b=0; b<N; b++){
            cout << board[a][b] <<  " ";
        }
        cout << endl;
    }
}

bool isSafe(int board[N][N], int row, int col, int num){
    for (int i=0; i<N; i++){
        if ((i!=row)&&(board[i][col] == num)){ return false;}
    }
    for (int j=0; j<N; j++){
        if ((j!=col)&&(board[row][j] == num)){ return false;}
    }
    int startingRow = (N/3)*(row/(N/3));
    int startingCol = (N/3)*(col/(N/3));
    for (int a=startingRow; a<startingRow+3; a++){
        for (int b=startingCol; b<startingCol+3; b++){
            if (((a!=row)||(b!=col))&&(board[a][b] == num)){ return false;}
        }
    }
    return true;
}

pair<int, int> getUnassigned(int board[N][N], int row, int col){
    for (int a=row; a<N; a++){
        for (int b=0; b<N; b++){
            if (board[a][b] == 0){ return (make_pair(a,b));}
        }
    }
    return (make_pair(-1,-1));
}

bool solve(int board[N][N], int row, int col){
    pair<int,int> unassigned = getUnassigned(board, row, col);
    if (unassigned.first == -1) { return true; }
  //  cout << unassigned.first << "," << unassigned.second << endl;
    
    for (int i=1;i<=N; i++){
        if (isSafe(board, unassigned.first, unassigned.second, i)){
         //   cout << i << " is safe" << endl;
            board[unassigned.first][unassigned.second] = i;
            if ((unassigned.first==N-1)&&(unassigned.second==N-1)){ return true; }
            else if (unassigned.second==N-1){ 
                if(solve(board, unassigned.first+1, 0)) { return true; } 
            }
            else{ 
                if (solve(board, unassigned.first, unassigned.second+1)) { return true; } 
            }
        }
    }
    board[unassigned.first][unassigned.second] = 0;
//    cout << "backtrack from " << unassigned.first << "," << unassigned.second << endl;
    return false;
}

int main(int argc, char **argv){

    int board[N][N] = {{0, 8, 4, 1, 0, 0, 0, 0, 0}, 
                       {3, 0, 0, 0, 0, 0, 0, 2, 0}, 
                       {7, 0, 0, 9, 0, 0, 0, 0, 0}, 
                       {0, 2, 0, 8, 0, 3, 0, 1, 6}, 
                       {0, 0, 0, 0, 0, 7, 9, 0, 3}, 
                       {6, 0, 0, 0, 0, 9, 5, 0, 0}, 
                       {0, 1, 0, 0, 6, 0, 0, 0, 5}, 
                       {2, 0, 0, 0, 0, 0, 0, 6, 1}, 
                       {0, 0, 0, 0, 0, 0, 0, 0, 0}};

 /*   int board[N][N] = {{7, 0, 0, 0, 0, 0, 0, 0, 0}, 
                       {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
                       {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
                       {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
                       {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
                       {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
                       {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
                       {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
                       {0, 0, 0, 0, 0, 0, 0, 0, 0}};*/

    printBoard(board);
  //  cout << getUnassigned(board, 2, 2).first << getUnassigned(board, 2, 2).second << endl;
    if (!solve(board, 0, 0)) { cout << "Not Solvable!!" << endl; }
    else{ printBoard(board); }

   //cout << isSafe(board, 1, 0, 2) << endl;
    

}
