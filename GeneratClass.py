#!/usr/bin/python

import sys

# Generate class with canonical form

def GenerateClass(list):
    for value in list:
        with open(value + '.hpp', 'w') as f:
            headerFile = "#ifndef " + value.upper() + "_CLASS\n"
            headerFile += "#define " + value.upper() + "_CLASS\n\n"
            headerFile += "#include <iostream>\n\n"
            headerFile += "class " + value + "\n"
            headerFile += "{\n"
            headerFile += "public:\n"
            headerFile += "\t" + value + "();\n"
            headerFile += "\t" + "~" + value + "();\n"
            headerFile += "\t" + value + "(const " + value + " &" + value[0].lower() + ");\n"
            headerFile += "\t" + value + " & operator =" + "(const " + value + " &" + value[0].lower() + ");\n"
            headerFile += "private: \n\n"
            headerFile += "}; \n\n"
            headerFile += "#endif // !" + value.upper() + "_CLASS \n"
            f.write(headerFile)
    for value in list:
        with open(value + '.cpp', 'w') as f:
            cppFile = "#include \"" + value + ".hpp\"\n\n"
            cppFile += value + "::" + value + "(){\n"
            cppFile += "\t" + "std::cout << \"Default constructor called\" << std::endl;\n"
            cppFile += "} \n\n"
            cppFile += value + "::~" + value + "(){\n"
            cppFile += "\t" + "std::cout << \"Destructor called\" << std::endl;\n"
            cppFile += "} \n\n"
            cppFile += value + "::" + value + "(const " + value + " &" + value[0].lower() + "){\n"
            cppFile += "\t" + "std::cout << \"Copy constructor called\" << std::endl;\n"
            cppFile += "\t *this = " + value[0].lower() + ";\n"
            cppFile += "} \n\n"
            cppFile += value + " & "  + value + "::operator =" + "(const " + value + " &" + value[0].lower() + "){\n"
            cppFile += "\t" + "std::cout << \"Copy assignment operator called\" << std::endl;\n"
            cppFile += "\tif(this != &" + value[0].lower() + ")\n"
            cppFile += "\t{ \n"
            cppFile += "\t} \n"
            cppFile += "\treturn *this;\n"
            cppFile += "} \n\n"
            f.write(cppFile)

if (len( sys.argv ) > 1):
    GenerateClass(sys.argv[1].split(','))
