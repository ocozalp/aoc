package gsu.crypt.quiz1_3;

import static gsu.crypt.util.Utils.*;

import java.util.Hashtable;
import java.util.Scanner;

public class NewCaesarBoxCipherDecryptor {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter key : ");
		String key = scanner.nextLine();
		
		System.out.print("Enter encrypted text : ");
		String encryptedText = scanner.nextLine();
		
		int [] indexes = getIndexArray(key);
		printIndexes(key, indexes);
		
		Hashtable<Integer, Integer> columnHash = getColumnHash(encryptedText.length(), indexes);
		Hashtable<Integer, Integer> reverseHash = getReverseHash(indexes);
		
		String decryptedText = getDecryptedText(encryptedText, indexes, columnHash, reverseHash);
		
		System.out.println(decryptedText);
		
		scanner.close();
	}
	
	private static Hashtable<Integer, Integer> getReverseHash(int[] indexes) {
		Hashtable<Integer, Integer> reverse = new Hashtable<Integer, Integer>();
		for(int i = 0; i<indexes.length; ++i) {
			reverse.put(indexes[i] - 1,	i);
		}
		
		return reverse;
	}

	private static String getDecryptedText(String encryptedText, int[] indexes, 
			Hashtable<Integer, Integer> columnHash, Hashtable<Integer, Integer> reverseHash) {
		
		String [] stringArray = new String[indexes.length];
		
		int colCount = encryptedText.length() / indexes.length;
		boolean isSquare = colCount * indexes.length == encryptedText.length();
		int contentIndex = 0;
		
		for(int i = 0; i<indexes.length; ++i) {
			int length = columnHash.get(i);
			
			String temp = encryptedText.substring(contentIndex, contentIndex + length);
			contentIndex += length;
			stringArray[reverseHash.get(i)] = temp;
		}
		
		return getDecryptedContentFromArray(stringArray, isSquare, colCount);
	}

	private static String getDecryptedContentFromArray(String[] stringArray, boolean isSquare, int colCount) {
		colCount = isSquare ? colCount : colCount+1;
		StringBuffer buffer = new StringBuffer();
		
		for(int i = 0; i<colCount; ++i) {
			for(int j = 0; j<stringArray.length; ++j) {
				if(stringArray[j].length() > i)
					buffer.append(stringArray[j].substring(i, i+1));
			}
		}
		return buffer.toString();
	}

	private static Hashtable<Integer, Integer> getColumnHash(int contentLength, int[] indexes) {
		Hashtable<Integer, Integer> result = new Hashtable<Integer, Integer>();
		int colCount = contentLength / indexes.length;
		int fullColumnCount = contentLength - colCount * indexes.length;
		
		for(int i = 0; i<indexes.length; ++i) {
			result.put(indexes[i] - 1, i<fullColumnCount ? colCount + 1 : colCount);
		}
		
		return result;
	}

	private static void printIndexes(String key, int[] indexes) {
		System.out.println(key);
		for(int i = 0; i<indexes.length; ++i) {
			System.out.print(indexes[i] + "~");
		}
		System.out.println();
	}

	private static int[] getIndexArray(String key) {
		int [] indexes = new int[key.length()];
		int alphabetLength = ALPHABET.length();
		int keyLength = key.length();
		
		int foundLetters = 0;
		for(int i = 0; foundLetters < keyLength && i<alphabetLength; ++i) {
			String letter = ALPHABET.substring(i, i+1);
			int index = -1;
			
			while((index = key.indexOf(letter, index + 1)) >= 0) {
				foundLetters++;
				indexes[index] = foundLetters;
			}
		}
		
		return indexes;
	}
}
