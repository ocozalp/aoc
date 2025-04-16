package gsu.crypt.quiz1_2;

import static gsu.crypt.util.Utils.*;

import java.util.Scanner;

public class NewCaesarBoxCipher {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter plain text : ");
		String content = scanner.nextLine();
		
		System.out.print("Enter key : ");
		String key = scanner.nextLine();
		
		int [] indexes = getIndexArray(key);
		
		printIndexes(key, indexes);
		
		String result = getEncryptedTextWithIndexes(content, indexes);
		
		System.out.println(result);
		
		scanner.close();
	}

	private static String getEncryptedTextWithIndexes(String content, int[] indexes) {
		int rowCount = getRowCount(content, indexes.length);
		int contentLength = content.length();
		String [] stringArray = new String[indexes.length];
		
		for(int i = 0; i<indexes.length; ++i) {
			String temp = "";
			for(int j = 0; j<rowCount; ++j) {
				int index = j * indexes.length + i;
				if(index < contentLength)
					temp += content.substring(index, index + 1);
			}
			stringArray[indexes[i] - 1] = temp;
		}
		
		return getEncryptedContentFromArray(stringArray);
	}

	private static String getEncryptedContentFromArray(String[] stringArray) {
		StringBuffer buffer = new StringBuffer();
		for(int i = 0; i<stringArray.length; ++i) {
			buffer.append(stringArray[i]);
		}
		
		return buffer.toString();
	}

	private static int getRowCount(String content, int length) {
		int contentLength = content.length();
		int result = contentLength / length;
		return result * length == contentLength ? result : result + 1;
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
