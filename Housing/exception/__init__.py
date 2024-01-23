import sys
import os

def error_message_detail(error_message:Exception,error_detail:sys)->str:
    _,_,exec_tb=error_detail.exec_info()
    line_number=exec_tb.tb_lineno
    file_name=exec_tb.tb_frame.f_code.co_filename
    exception_line_number=exec_tb.tb_frame.f_lineno
    error_message=f"the error occured in the script {file_name} line number {line_number} exception line number {exception_line_number} message : {error_message}. "
    return error_message
    


class CustomException(Exception):
    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message=error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message
    
    def __repr__(self)->str:
        return CustomException.__name__.str()
    
           