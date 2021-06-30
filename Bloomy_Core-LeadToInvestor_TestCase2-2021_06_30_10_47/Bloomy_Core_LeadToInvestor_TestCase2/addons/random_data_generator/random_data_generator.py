from .actions import GenerateAge, GenerateAltitude, GenerateBirthday, GenerateBoolean, GenerateChar, GenerateCity, GenerateCountry, GenerateCredicardExpiry, GenerateCredicardNumber, GenerateCredicardType, GenerateCredicardVV, GenerateDecimal, GenerateDepth, GenerateDouble, GenerateFirstName, GenerateFloat, GenerateGender, GenerateLastName, GenerateLatitude, GenerateLongitude, GenerateLoremIpsum, GenerateName, GenerateNatural, GenerateNumberInRange, GenerateParagraph, GeneratePostcode, GeneratePrefix, GenerateSentence, GenerateStreet, GenerateString, GenerateSyllable, GenerateWord


class RandomDataGenerator:
    @staticmethod
    def generateage() -> GenerateAge:
        """Generate random age.

        Generates random age.
        """
        return GenerateAge()

    @staticmethod
    def generatealtitude() -> GenerateAltitude:
        """Generate random altitude.

        Generates random altitude.
        """
        return GenerateAltitude()

    @staticmethod
    def generatebirthday() -> GenerateBirthday:
        """Generate random birthday.

        Generates random birthday.
        """
        return GenerateBirthday()

    @staticmethod
    def generateboolean() -> GenerateBoolean:
        """Generate random boolean.

        Generates random boolean.
        """
        return GenerateBoolean()

    @staticmethod
    def generatechar() -> GenerateChar:
        """Generate random char.

        Generates random char.
        """
        return GenerateChar()

    @staticmethod
    def generatecity() -> GenerateCity:
        """Generate random city.

        Generates random city.
        """
        return GenerateCity()

    @staticmethod
    def generatecountry() -> GenerateCountry:
        """Generate random country.

        Generates random country.
        """
        return GenerateCountry()

    @staticmethod
    def generatecredicardexpiry() -> GenerateCredicardExpiry:
        """Generate random credit-card expiry date.

        Generates random credit-card expiry date.
        """
        return GenerateCredicardExpiry()

    @staticmethod
    def generatecredicardnumber() -> GenerateCredicardNumber:
        """Generate random credit-card number.

        Generates random credit-card number.
        """
        return GenerateCredicardNumber()

    @staticmethod
    def generatecredicardtype() -> GenerateCredicardType:
        """Generate random credit-card type.

        Generates random credit-card type.
        """
        return GenerateCredicardType()

    @staticmethod
    def generatecredicardvv() -> GenerateCredicardVV:
        """Generate random credit-card verification value.

        Generates random credit-card verification value.
        """
        return GenerateCredicardVV()

    @staticmethod
    def generatedecimal() -> GenerateDecimal:
        """Generate random decimal.

        Generates random decimal.
        """
        return GenerateDecimal()

    @staticmethod
    def generatedepth() -> GenerateDepth:
        """Generate random depth.

        Generates random depth.
        """
        return GenerateDepth()

    @staticmethod
    def generatedouble() -> GenerateDouble:
        """Generate random double.

        Generates random double.
        """
        return GenerateDouble()

    @staticmethod
    def generatefirstname() -> GenerateFirstName:
        """Generate random first name.

        Generates random first name.
        """
        return GenerateFirstName()

    @staticmethod
    def generatefloat() -> GenerateFloat:
        """Generate random float.

        Generates random float.
        """
        return GenerateFloat()

    @staticmethod
    def generategender() -> GenerateGender:
        """Generate random gender.

        Generates random gender.
        """
        return GenerateGender()

    @staticmethod
    def generatelastname() -> GenerateLastName:
        """Generate random last name.

        Generates random last name.
        """
        return GenerateLastName()

    @staticmethod
    def generatelatitude() -> GenerateLatitude:
        """Generate random latitude.

        Generates random latitude.
        """
        return GenerateLatitude()

    @staticmethod
    def generatelongitude() -> GenerateLongitude:
        """Generate random longitude.

        Generates random longitude.
        """
        return GenerateLongitude()

    @staticmethod
    def generateloremipsum() -> GenerateLoremIpsum:
        """Generate random lorem ipsum.

        Generates random lorem ipsum.
        """
        return GenerateLoremIpsum()

    @staticmethod
    def generatename() -> GenerateName:
        """Generate random name.

        Generates random name.
        """
        return GenerateName()

    @staticmethod
    def generatenatural() -> GenerateNatural:
        """Generate random natural.

        Generates random natural.
        """
        return GenerateNatural()

    @staticmethod
    def generatenumberinrange(min: str, max: str) -> GenerateNumberInRange:
        """Generate random number between {{min}} and {{max}}.

        Generates random number between a specified range.
        """
        return GenerateNumberInRange(min, max)

    @staticmethod
    def generateparagraph() -> GenerateParagraph:
        """Generate random paragraph.

        Generates random paragraph.
        """
        return GenerateParagraph()

    @staticmethod
    def generatepostcode() -> GeneratePostcode:
        """Generate random postcode.

        Generates random postcode.
        """
        return GeneratePostcode()

    @staticmethod
    def generateprefix() -> GeneratePrefix:
        """Generate random prefix.

        Generates random prefix.
        """
        return GeneratePrefix()

    @staticmethod
    def generatesentence() -> GenerateSentence:
        """Generate random sentence.

        Generates random sentence.
        """
        return GenerateSentence()

    @staticmethod
    def generatestreet() -> GenerateStreet:
        """Generate random street.

        Generates random street.
        """
        return GenerateStreet()

    @staticmethod
    def generatestring() -> GenerateString:
        """Generate random string.

        Generates random string.
        """
        return GenerateString()

    @staticmethod
    def generatesyllable() -> GenerateSyllable:
        """Generate random syllable.

        Generates random syllable.
        """
        return GenerateSyllable()

    @staticmethod
    def generateword() -> GenerateWord:
        """Generate random word.

        Generates random word.
        """
        return GenerateWord()
