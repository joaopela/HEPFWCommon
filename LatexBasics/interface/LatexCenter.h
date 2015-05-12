#ifndef LATEX_ALIGNMENT_LATEXCENTER
#define LATEX_ALIGNMENT_LATEXCENTER

#include "HEPFWCommon/LatexCore/interface/LatexEnvironment.h"

// C++ Included
#include <string>

namespace hepfw{
  
  /***********************************************/
  /** \brief 
   * 
   * 
   ***********************************************/
  class LatexCenter : public LatexEnvironment{
  public:
    
    LatexCenter();
    ~LatexCenter(){};
    
  private:
    
    void init();
    
  };
  
}

#endif