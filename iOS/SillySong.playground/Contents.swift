import UIKit

func shortNameFromName(_ name:String) -> String {
    var lowercaseName = name.lowercased().folding(options: .diacriticInsensitive, locale: .current)
    var vowels = CharacterSet(charactersIn: "aeiou")
    var firstVowelIndex = lowercaseName.rangeOfCharacter(from:vowels)
    lowercaseName.substring(from:firstVowelIndex)
    return "tmp"
}

shortNameFromName("Andy")