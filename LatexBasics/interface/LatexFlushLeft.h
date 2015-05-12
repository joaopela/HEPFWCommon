#ifndef LATEX_ALIGNMENT_LATEXFLUSHLEFT
#define LATEX_ALIGNMENT_LATEXFLUSHLEFT

#include "HEPFWCommon/LatexCore/interface/LatexEnvironment.h"

// C++ Included
#include <string>

namespace hepfw{
  
  /***********************************************/
  /** \brief 
   * 
   * 
   ***********************************************/
  class LatexFlushLeft : public LatexEnvironment{
  public:
    
    LatexFlushLeft();    
    ~LatexFlushLeft(){};
    
  private:
    
    void init();
    
  };
  
}

#endif