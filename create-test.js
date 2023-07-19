const path = require('path');
const fs = require('fs');

// The first argument to the script is the path to the TypeScript or HTML file
const filePath = process.argv[2];

// Read the file
fs.readFile(filePath, 'utf8', function(err, fileContent) {
    if (err) {
        console.error(`Error reading file ${filePath}:`, err);
        return;
    }

    // Pretend to send the file content to the OpenAI API
    console.log(`Sending content to OpenAI API: ${fileContent}`);

    // The API would return the unit test code
    // For now, just log a fake response
    const fakeApiResponse = 'describe("My Component", function() { it("should do something", function() { expect(true).toBe(true); }); });';

    console.log(`Received unit test code from OpenAI API: ${fakeApiResponse}`);

    // Get the directory of the file
    const dirName = path.dirname(filePath);

    // Get the base name of the file
    const baseName = path.basename(filePath, path.extname(filePath));

    // Construct the spec file path
    const specFilePath = path.join(dirName, baseName + '.spec.ts');

    // Write the unit test code to the .spec.ts file
    fs.writeFile(specFilePath, fakeApiResponse, function(err) {
        if (err) {
            console.error(`Error writing to file ${specFilePath}:`, err);
            return;
        }

        console.log(`Successfully wrote unit test to ${specFilePath}`);
    });
});
