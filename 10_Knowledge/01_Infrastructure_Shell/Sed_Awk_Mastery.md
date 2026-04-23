# Sed and Awk Mastery
Phase Phase 1

## 1. The Mental Model
- **Sed (Stream Editor):** A non-interactive editor that performs transformations on a stream of text. Think of it as "Search and Replace on steroids." It works line-by-line.
- **Awk (Text Processor):** A full programming language designed for data extraction and reporting. Think of it as "Command-line Excel." It sees lines as **Records** and words as **Fields**.

## 2. Technical Deep Dive
### Sed: The Surgeon
- **Substitute:** `sed 's/old/new/g' file` (g = global).
- **Delete Lines:** `sed '3d' file` (delete line 3).
- **In-place Edit:** `sed -i 's/foo/bar/g' file` (Dangerous: modifies the file directly).
- **Regex Power:** `sed -E 's/([0-9]+)/<\1>/g'` (Wrap numbers in brackets).

### Awk: The Accountant
- **Print Fields:** `awk '{print $1, $3}' file` (Print 1st and 3rd columns).
- **Conditionals:** `awk '$3 > 50 {print $1}' file` (Print 1st col if 3rd col > 50).
- **Calculations:** `awk '{sum += $3} END {print sum}' file` (Sum the 3rd column).
- **Field Separator:** `awk -F':' '{print $1}' /etc/passwd` (Use `:` as delimiter).

## 3. Mastery Drills
### Terminal Challenges
1. **The Config Scrubber:** Use `sed` to remove all commented lines (starting with `#`) and all empty lines from a configuration file.
2. **The Log Parser:** Use `awk` on a web server log (or fake one) to find the top 3 IP addresses with the most requests.
   - *Hint:* `awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -3`

### Edge Cases
- **Sed Delimiters:** You don't have to use `/`. If you are editing URLs, use `sed 's|http://|https://|g'`. 
- **Awk $0:** `$0` represents the entire line.

## 4. Execution Contract
- **Timebox:** 45 minutes
- **Start Command:** `seq 1 100 > numbers.txt`
- **Completion Condition:** Use `sed` to replace all even numbers with the word "EVEN" and then use `awk` to count how many times "EVEN" appears.
