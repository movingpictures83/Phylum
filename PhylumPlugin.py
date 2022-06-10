import PyPluMA

def unquote(s):
   return s[1:len(s)-1]

class PhylumPlugin:
    def input(self, infile):
       inputfile = open(infile, 'r')
       params = dict()
       for line in inputfile:
           contents = line.strip().split('\t')
           params[contents[0]] = contents[1]
       self.taxfile = open(PyPluMA.prefix()+"/"+params['taxfile'], 'r')
       self.csvfile = open(PyPluMA.prefix()+"/"+params['csvfile'], 'r')

    def run(self):
       self.taxa = []
       self.taxfile.readline()
       for line in self.taxfile:
           contents = line.strip().split(',')
           self.taxa.append(contents)
       firstline = self.csvfile.readline()
       self.bac = firstline.strip().split(',')
       self.bac = self.bac[1:]

    def output(self, outfile):
       outputfile = open(outfile, 'w')
       outputfile.write("Name\tPhylum\n")
       for i in range(0, len(self.bac)):
          bacter = self.bac[i]
          #if ("(Kingdom)" in bacter):
          #    bacter.remove("(Kingdom)")
          #if ("(Phylum)" in bacter):
          #    bacter.remove("(Phylum)")
          #if ("(Class)" in bacter):
          #    bacter.remove("(Class)")
          #if ("(Order)" in bacter):
          #    bacter.remove("(Order)")
          #if ("(Family)" in bacter):
          #    bacter.remove("(Family)")
          #if ("(Genus)" in bacter):
          #    bacter.remove("(Genus)")
          #if ("(Species)" in bacter):
          #    bacter.remove("(Species)")
          phylum = "None"
          for j in range(len(self.taxa)):
              for k in range(len(self.taxa[j])):
                  if (self.taxa[j][k] == bacter):
                      phylum = self.taxa[j][2]
                      break
          if (phylum == "None"):
             print("WARNING NONE PHYLUM FOR: "+self.bac[i])
          outputfile.write(unquote(self.bac[i])+"\t"+unquote(phylum)+"\n")

