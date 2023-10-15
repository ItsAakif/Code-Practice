#include <iostream>
using namespace std;

/*
	Given the coordinates of rectange in clockwise direction, check if it is a valid rectangle or not.
	Each coordinate is a pair of (x,y) and there are 4 such pairs.
*/

string validateRect(float arr[4][2]) {
	if((arr[0][0] == arr[1][0]) && (arr[2][0] == arr[3][0]) && (arr[0][1] == arr[3][1]) && (arr[1][1] == arr[2][1]))
			return "Valid";
	else if((arr[0][0] == arr[3][0]) && (arr[1][0] == arr[2][0]) && (arr[0][1] == arr[1][1]) && (arr[2][1] == arr[3][1]))
			return "Valid";
	return "Invalid";
}

int main() {
	float arr[4][2], zero_coordinate = 0;

	// Input
	for(int i=0; i<4; i++) {
		for(int j=0; j<2; j++) {
			cin >> arr[i][j];

			if(arr[i][j] == 0)
					zero_coordinate += 1;
		}
	}

	if(zero_coordinate == 8)
		cout << "Invalid" << endl;
	else
		cout << validateRect(arr) << endl;

    return 0;
}
