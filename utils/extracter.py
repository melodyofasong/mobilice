import pandas as pd
import phonenumbers
from phonenumbers import PhoneNumberMatcher, PhoneNumberType

def phonenums(x):
    matcher = PhoneNumberMatcher(x, "IN")
    
    type_map = {
        PhoneNumberType.MOBILE: "mobile",
        PhoneNumberType.FIXED_LINE: "landline",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "unknown",
    }
    
    phones = []
    seen = set()
    
    for match in matcher:
        formatted = phonenumbers.format_number(
            match.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        if formatted in seen:
            continue
        seen.add(formatted)
        
        num_type = type_map.get(phonenumbers.number_type(match.number), "unknown")
        phones.append({"Phone Number": formatted, "Type": num_type})
    
    df = pd.DataFrame(phones)
    df.index += 1
    return df
