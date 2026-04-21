# Web Browse Skill

## Purpose
This skill enables the agent to retrieve the raw content of a web page from a given URL using the `curl` command. This is useful for fetching static information, API responses, or the source HTML of a webpage.

## Limitations
-   **No JavaScript Execution**: This skill does not execute JavaScript. Websites heavily reliant on client-side rendering will not be fully browsed.
-   **No Visual Rendering**: This is a text-based retrieval. There is no graphical rendering of the web page.
-   **No Interaction**: Cannot click links, fill forms, or interact with dynamic elements on a page.
-   **Rate Limiting/Blocking**: Websites may block `curl` requests or implement rate limiting.
-   **Cookies/Sessions**: Handling complex session management or cookies is not directly supported without manual `curl` flag configuration.

## Procedure

### Step 1: Identify the URL
Determine the exact URL of the web page or resource you wish to retrieve.

### Step 2: Execute the `curl` Command
Use the `bash` tool to execute `curl` with the desired URL.

#### Basic Usage (Fetch entire page content):
```bash
curl "https://example.com"
```
The output will be the raw HTML or content of the page, which will be returned as `stdout`.

#### Saving to a File (Optional):
If the content is large or you want to process it later, you can save it to a file:
```bash
curl "https://example.com" -o "output.html"
```
The content will be saved to `output.html` in the current working directory. You can then `read` this file.

#### Following Redirects:
To automatically follow HTTP 3xx redirects, use the `-L` flag:
```bash
curl -L "https://shorturl.at/abcde"
```

#### Including HTTP Headers:
To see the HTTP response headers (useful for debugging or understanding server responses), use the `-i` flag:
```bash
curl -i "https://example.com"
```

#### Suppressing Progress Meter:
To prevent `curl` from showing a progress bar in `stderr`, use the `-s` (silent) flag:
```bash
curl -s "https://example.com"
```
Often, `-sL` is used together for silent output and following redirects.

### Step 3: Process the Retrieved Content
Once the content is retrieved (either in `stdout` or a file), use other available tools (like `read`, `grep`, `edit` if writing to a file, or your internal reasoning) to analyze or extract information.

## Example Usage by Agent:

**Agent Goal**: Find the latest news headlines from a specific tech blog.
**Agent Action**:
1.  Identify blog URL: `https://techblog.example.com/`
2.  Execute `curl` to fetch content:
    ```bash
    curl -sL "https://techblog.example.com/"
    ```
3.  Analyze the `stdout` for relevant headlines using pattern matching or by identifying HTML structure.

---

**Note to Agent**: Always consider the ethical implications and terms of service of the website before attempting to retrieve content programmatically. Avoid excessive requests to prevent overwhelming the server.
