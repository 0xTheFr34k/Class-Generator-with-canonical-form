#!/usr/bin/python

# Generate class with canonical form

import sys

if (len( sys.argv ) > 1):
    className = sys.argv[1]
# generate header file
    with open(className.capitalize() + '.hpp', 'w') as f:
        headerFile = "#ifndef " + className.upper() + "_CLASS\n"
        headerFile += "#define " + className.upper() + "_CLASS\n\n"
        headerFile += "#include <iostream>\n\n"
        headerFile += "class " + className.capitalize() + "\n"
        headerFile += "{\n"
        headerFile += "public:\n"
        headerFile += "\t" + className.capitalize() + "();\n"
        headerFile += "\t" + "~" + className.capitalize() + "();\n"
        headerFile += "\t" + className.capitalize() + "(const " + className.capitalize() + " &" + className[0].lower() + ");\n"
        headerFile += "\t" + className.capitalize() + " & operator =" + "(const " + className.capitalize() + " &" + className[0].lower() + ");\n"
        headerFile += "private: \n\n"
        headerFile += "}; \n\n"
        headerFile += "#endif // !" + className.upper() + "_CLASS \n"
        f.write(headerFile)
# generate cpp file
    with open(className.capitalize() + '.cpp', 'w') as f:
        cppFile = "#include \"" + className.capitalize() + ".hpp\"\n\n"
        cppFile += className.capitalize() + "::" + className.capitalize() + "(){\n"
        cppFile += "\t" + "std::cout << \"Default constructor called\" << std::endl;\n"
        cppFile += "} \n\n"
        cppFile += className.capitalize() + "::~" + className.capitalize() + "(){\n"
        cppFile += "\t" + "std::cout << \"Destructor called\" << std::endl;\n"
        cppFile += "} \n\n"
        cppFile += className.capitalize() + "::" + className.capitalize() + "(const " + className.capitalize() + " &" + className[0].lower() + "){\n"
        cppFile += "\t" + "std::cout << \"Copy constructor called\" << std::endl;\n"
        cppFile += "\t *this = " + className[0].lower() + ";\n"
        cppFile += "} \n\n"
        cppFile += className.capitalize() + " & "  + className.capitalize() + "::operator =" + "(const " + className.capitalize() + " &" + className[0].lower() + "){\n"
        cppFile += "\t" + "std::cout << \"Copy assignment operator called\" << std::endl;\n"
        cppFile += "\tif(this != &" + className[0].lower() + ")\n"
        cppFile += "\t{ \n"
        cppFile += "\t} \n"
        cppFile += "\treturn *this;\n"
        cppFile += "} \n\n"
        f.write(cppFile)
else:
    print("please provide class Name")
