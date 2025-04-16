package gsu.crypt.quiz3_2;

import static gsu.crypt.util.Utils.*;

import java.util.ArrayList;
import java.util.Scanner;

public class SaccoCipherDecryptor {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter key : ");
		String key = scanner.nextLine();
		
		System.out.print("Enter encrypted text : ");
		String encryptedText = scanner.nextLine();
		
		String originalText = decryptText(encryptedText, key);
		
		System.out.println(originalText);
		
		scanner.close();
	}

	private static String decryptText(String encryptedText, String key) {
		int [] indexArray = getIndexArray(key);
		
		printIndexes(indexArray);
		
		int [] reverseIndexArray = getReverseIndexArray(indexArray);
		
		int [] lineLengthArray = getLineLengthArray(reverseIndexArray, encryptedText);
		
		String decryptedText = getDecryptedText(encryptedText, reverseIndexArray, lineLengthArray, indexArray);
		
		return decryptedText;
	}
	
	private static String getDecryptedText(String encryptedText, int[] reverseIndexArray, 
			int[] lineLengthArray, int [] indexArray) {
		int [] columnLengthArray = new int[indexArray.length];
		
		for(int i = 0; i<indexArray.length; ++i) {
			int maxLength = reverseIndexArray[indexArray[i] - 1];
			int colCount = 0;
			for(int j = 0; j<lineLengthArray.length; ++j) {
				if(lineLengthArray[j] >= maxLength)
					++colCount;
			}
			columnLengthArray[i] = colCount;
		}
		
		int currentIndex = 0;
		String [] columns = new String[indexArray.length];
		for(int i = 0; i<indexArray.length; ++i) {
			int length = columnLengthArray[reverseIndexArray[i] - 1];
			columns[reverseIndexArray[i] - 1] = encryptedText.substring(currentIndex, currentIndex + length);
			currentIndex += length;
		}
		
		String [] lines = new String[lineLengthArray.length];
		
		for(int i = 0; i<indexArray.length; ++i) {
			String column = columns[i];
			int columnLength = column.length();
			int foundChars = 0;
			for(int j = 0; j<lineLengthArray.length && foundChars < columnLength; ++j) {
				int size = j<reverseIndexArray.length ? reverseIndexArray[j] : 
					reverseIndexArray[reverseIndexArray.length - 1];
				
				if(size > i) {
					if(lines[j] == null)
						lines[j] = "";
					
					lines[j]+=column.substring(foundChars, ++foundChars); 
				}
			}
		}
		
		StringBuffer returnBuffer = new StringBuffer();
		for(int i = 0; i<lines.length; ++i)
			returnBuffer.append(lines[i]);
		
		return returnBuffer.toString();
	}

	private static int[] getLineLengthArray(int[] reverseIndexArray, String encryptedText) {
		int textLength = encryptedText.length();
		int index = 0;
		int charCount = 0;
		ArrayList<Integer> lengthList = new ArrayList<Integer>();
		
		while(charCount < textLength) {
			int arrayIndex = index < reverseIndexArray.length ? index : reverseIndexArray.length - 1;
			charCount += reverseIndexArray[arrayIndex];
			int lineLength = reverseIndexArray[arrayIndex];
			
			if(charCount > textLength) 
				lineLength -= charCount - textLength;
			
			lengthList.add(lineLength);
			
			++index;
		}
		
		int [] result = new int[index];
		for(int i = 0; i<index; ++i) {
			result[i] = lengthList.get(i);
		}
		return result;
	}

	private static int[] getReverseIndexArray(int[] indexArray) {
		int [] reverseArray = new int[indexArray.length];
		for(int i = 0; i<reverseArray.length; ++i) {
			reverseArray[indexArray[i] - 1] = i + 1;
		}
		return reverseArray;
	}

	private static void printIndexes(int[] indexArray) {
		for(int i = 0; i<indexArray.length; ++i) {
			System.out.print(indexArray[i] + " ");
		}
		System.out.println();
	}

	private static int[] getIndexArray(String key) {
		int alphabetLength = ALPHABET.length();
		int [] result = new int[key.length()];
		int foundLetterCount = 0;
		
		for(int i = 0; i<alphabetLength && foundLetterCount < result.length; ++i) {
			String letter = ALPHABET.substring(i, i+1);
			int index = -1;
			while( (index = key.indexOf(letter, index + 1)) != -1) {
				result[index] = ++foundLetterCount;
			}
		}
		return result;
	}
}
