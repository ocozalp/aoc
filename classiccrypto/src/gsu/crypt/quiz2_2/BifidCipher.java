package gsu.crypt.quiz2_2;

import static gsu.crypt.util.Utils.*;

import java.util.Scanner;

public class BifidCipher {
	
	public static void main(String[] args) {
		int rowSize = (int) Math.sqrt(ALPHABET.length());
		char [][] characterMatrix = buildRandomCharacterMatrix(rowSize);
		
		printCharacterMatrix(characterMatrix);
		
		String coordinateText = getCoordinateText(characterMatrix);
		
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter plain text : ");
		String text = scanner.nextLine();
		
		String encryptedText = encryptText(text, coordinateText, characterMatrix);
		
		System.out.println("Result : " + encryptedText);
		
		scanner.close();
	}

	private static String encryptText(String text, String coordinateText, char[][] characterMatrix) {
		int tildeIndex = coordinateText.indexOf("~");
		String rowText = coordinateText.substring(0, tildeIndex);
		String colText = coordinateText.substring(tildeIndex + 1);
		
		StringBuffer newRows = new StringBuffer();
		StringBuffer newCols = new StringBuffer();
		
		int count = text.length();
		StringBuffer buffer = new StringBuffer();
		
		for(int i = 0; i<count; ++i) {
			String letter = text.substring(i, i+1);
			int index = ALPHABET.indexOf(letter);
			
			int row = Integer.parseInt(rowText.substring(index, index + 1));
			int column = Integer.parseInt(colText.substring(index, index + 1));
			newRows.append(row);
			newCols.append(column);
		}
		
		System.out.println(newRows.toString());
		System.out.println(newCols.toString());
		String keyText = newRows.toString() + newCols.toString();
		
		for(int i = 0; i<count; ++i) {
			String coordinate = keyText.substring(i*2, i*2 + 2);
			int row = Integer.parseInt(coordinate.substring(0, 1)) - 1;
			int column = Integer.parseInt(coordinate.substring(1, 2)) - 1;
			buffer.append(characterMatrix[row][column]);
		}
		return buffer.toString();
	}

	private static String getCoordinateText(char[][] characterMatrix) {
		String rows = new String(ALPHABET);
		String columns = new String(ALPHABET);
		
		for(int i = 0; i<characterMatrix.length; ++i){
			for(int j = 0; j<characterMatrix.length; ++j) {
				char letter = characterMatrix[i][j];
				int index = rows.indexOf(letter);
				
				rows = rows.substring(0, index) + (String.valueOf(i+1)) + rows.substring(index + 1);
				columns = columns.substring(0, index) + (String.valueOf(j+1)) + columns.substring(index + 1);
			}
		}
		return rows + "~" + columns;
	}

	private static void printCharacterMatrix(char[][] characterMatrix) {
		System.out.print("\t");
		for(int i = 0; i<characterMatrix.length; ++i)
			System.out.print((i + 1) + " ");
		
		System.out.println();
		
		for(int i = 0; i<characterMatrix.length; ++i) {
			System.out.print((i+1) + "\t");
			for(int j = 0; j<characterMatrix.length; ++j) {
				System.out.print(characterMatrix[i][j] + " ");
			}
			System.out.println();
		}
	}

	private static char[][] buildRandomCharacterMatrix(int rowSize) {
		char[][] matrix = new char[rowSize][rowSize];
		int size = ALPHABET.length();
		int counter = 0;
		String cloneAlphabet = new String(ALPHABET);
		
		while(counter<size) {
			int randomIndex = (int) (Math.random() * size);
			char letter = cloneAlphabet.charAt(randomIndex);
			if(letter != ' ') {
				int row = counter / rowSize;
				int column = counter % rowSize;
				
				matrix[row][column] = letter;
				++counter;
				cloneAlphabet = cloneAlphabet.substring(0, randomIndex) + " " + 
					cloneAlphabet.substring(randomIndex + 1);
			}
		}
		
		return matrix;
	}
}