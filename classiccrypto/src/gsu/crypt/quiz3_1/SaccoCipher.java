package gsu.crypt.quiz3_1;

import static gsu.crypt.util.Utils.*;

import java.util.Scanner;
import java.util.StringTokenizer;

public class SaccoCipher {
	
	private static final String DELIMITER = ";";
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter key : ");
		String key = scanner.nextLine();
		
		System.out.print("Enter plain text : ");
		String text = scanner.nextLine();
		
		String encryptedText = encryptText(text, key);
		
		System.out.println(encryptedText);
		
		scanner.close();
	}

	private static String encryptText(String text, String key) {
		int [] indexArray = getIndexArray(key);
		
		printIndexes(indexArray);
		
		int [] reverseIndexArray = getReverseIndexArray(indexArray);
		
		String delimitedText = getDelimitedText(text, reverseIndexArray);
		
		String [] tokens = getTokenArray(delimitedText);
		String encryptedText = getEncryptedTextFromTokenArray(tokens, reverseIndexArray);
		
		return encryptedText;
	}

	private static String getEncryptedTextFromTokenArray(String[] tokens, int[] reverseIndexArray) {
		StringBuffer buffer = new StringBuffer();
		for(int i = 0; i<reverseIndexArray.length; ++i) {
			for(int j = 0; j<tokens.length; ++j) {
				if(tokens[j].length() >= reverseIndexArray[i]) {
					buffer.append(tokens[j].substring(reverseIndexArray[i] - 1, reverseIndexArray[i]));
				}
			}
		}
		return buffer.toString();
	}

	private static String[] getTokenArray(String delimitedText) {
		StringTokenizer st = new StringTokenizer(delimitedText, DELIMITER);
		String [] result = new String[st.countTokens()];
		int i = 0;
		while(st.hasMoreTokens()){
			result[i++] = st.nextToken();
		}
		
		return result;
	}

	private static String getDelimitedText(String text, int[] reverseIndexArray) {
		int lineCount = 0;
		int encryptedCharacterCount = 0;
		int textLength = text.length();
		StringBuffer buffer = new StringBuffer();
		
		while(encryptedCharacterCount < textLength) {
			int index = lineCount >= reverseIndexArray.length ? reverseIndexArray.length - 1 : lineCount;
			int tokenLength = reverseIndexArray[index];
			String line;
			if(encryptedCharacterCount + tokenLength > textLength) {
				line = text.substring(encryptedCharacterCount);
			} else {
				line = text.substring(encryptedCharacterCount, encryptedCharacterCount + tokenLength);
			}
			
			buffer.append(line).append(DELIMITER);
			
			encryptedCharacterCount += tokenLength;
			++lineCount;
		}
		return buffer.toString();
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
